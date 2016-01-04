import time
import os
from decimal import *
import shutil
from Tkinter import *
from tkFileDialog import *
import ConfigParser
from ConfigParser import SafeConfigParser
import urlparse
import zipfile
import urllib2
import urllib
import sys


thisver = 201601042350

def spacetime ():
    time.sleep(2)
    clear()

def menerror():
    clear()
    print "Please choose an option from the menu..."
    time.sleep(2)
    clear()
 

clear = lambda: os.system('cls')

ft = 'frame-template '
sft = 'subframe-template '
strt = '-s '
end = '-e '
pu = 'push'
sb = ' '
i = '-i '
n = '-N '
p = '-p '
spot = 'spot'
spotprice = 'price'

py = 'python '
bw = 'brenda-work '
br = 'brenda-run '
bt = 'brenda-tool '
sh = 'ssh '
ut = 'uptime '
st = 'status'
pf = 'perf'
tc = 'cat task-count'
tl = 'tail log'
pru = 'prune '
smlt = '-t '
dflag = '-d '
xsize = '-X '
ysize = '-Y '

rs = 'reset'
t = '-T '
sp = 'stop'
ca = 'cancel'
bm = 'c:/brenda-master'
ps = 'c:/Python27/Scripts'
ap = '/AppData/Roaming/'
ini = 's3cmd.ini'
sl = '/'
scf = '.s3cfg'
brenda = 'brenda'
q = '"'
ff = '-F'

sys.path.insert(0, bm+sl+brenda)
import ami


os.chdir(bm)




def mainmenuoptions ():
    print
    print
    print
    print
    print "s = Setting up your farm"
    print "m = Managing your farm"
    print "d = Download rendered frames"
    print "c = Canceling and resetting your farm"
    print
    print

def mainmenu ():
    while True:
        clear()
        mainmenuoptions ()
        submen = raw_input('Which task would you like to perform? ')
        if submen =='s':           
            setupmenu()    
        if submen =='m':           
            monmenu()
        if submen =='d':
            downmenu()   
        if submen =='c':           
            cancelmenu()

             

def setupmenuoptions ():
    print 
    print "m = Go to main menu"
    print
    print
    print "u = Update AMI"
    print "n = New project upload"
    print "f = Frame settings"
    print "b = Build work queue"
    print "p = Price of instance"
    print "j = Job summary"
    print "i = Initiate instances"
    print
    print


def amis ():
    clear()
    urllib.urlretrieve ("http://www.thegreyroompost.com/win_brenda/win_brenda.ini", "win_brenda.ini")
    parser = SafeConfigParser()
    parser.read('win_brenda.ini')
    adesc = parser.get('amis', 'amidesca')
    a = parser.get('amis', 'amia')
    bdesc = parser.get('amis', 'amidescb')
    b = parser.get('amis', 'amib')
    cdesc = parser.get('amis', 'amidescc')
    c = parser.get('amis', 'amic')
    os.remove('win_brenda.ini')
    reload(ami)

    while True:
        clear()
        print
        print 'Current AMI = '+ami.AMI_ID
        print
        print
        print
        print 'Recommended compatible AMIs...'
        print
        print
        print "a = "+adesc
        print
        print "b = "+bdesc
        print
        print "c = "+cdesc
        print
        print
        print
        amiconf = raw_input('Choose an AMI or enter "e" to input your own: ')
        if amiconf =='a':
            clear()
            print
            print "Updating AMI..."
            os.chdir(bm+sl+brenda)
            file = open("ami.py", "w")
            w = """# An AMI that contains Blender and Brenda (may be None)
AMI_ID="""
            file.write(w+q+a+q)
            file.close()
            spacetime ()
            print
            print "AMI Updated"
            spacetime()
            break
        if amiconf =='b':
            clear()
            print
            print "Updating AMI..."
            os.chdir(bm+sl+brenda)
            file = open("ami.py", "w")
            w = """# An AMI that contains Blender and Brenda (may be None)
AMI_ID="""
            file.write(w+q+b+q)
            file.close()
            spacetime ()
            print
            print "AMI Updated"
            spacetime()
            break
        if amiconf =='c':
            clear()
            print
            print "Updating AMI..."
            os.chdir(bm+sl+brenda)
            file = open("ami.py", "w")
            w = """# An AMI that contains Blender and Brenda (may be None)
AMI_ID="""
            file.write(w+q+c+q)
            file.close()
            spacetime ()
            print
            print "AMI Updated"
            spacetime()
            break
        if amiconf =='e':
            clear()
            print
            ami_user = raw_input('Enter the new public AMI you wish to use: ')
            clear()
            print
            print 'Your new AMI will be changed to '+q+ami_user+q
            print
            print
            amiconf = raw_input('Do you want to continue, type y or n? ') 
            if amiconf=='y':
                clear()
                print
                print "Updating AMI..."
                os.chdir(bm+sl+brenda)
                file = open("ami.py", "w")
                w = """# An AMI that contains Blender and Brenda (may be None)
AMI_ID="""
                file.write(w+q+ami_user+q)
                file.close()
                spacetime ()
                print
                print "AMI Updated"
                spacetime()
                os.chdir(bm)
                break
            if amiconf=='n':
                clear()
                break

def nproj ():
    while True:
        print
        print "Select your Blender project file (must be packed)..."
        time.sleep(1)
        root = Tk()
        root.withdraw()
        projfile = askopenfilename(parent=root, title='select your packed Blender project file')
        root.destroy()
        clear()
        projfilename = os.path.basename(os.path.abspath(projfile))
        projfilepath = os.path.dirname(os.path.abspath(projfile))
        print
        print "***WARNING***"
        print
        print
        print "This will..." 
        print
        print
        print "1. delete all files in your frame and project buckets"
        print
        print "2. zip and upload "+projfilename
        print
        print "3. reset work queue"
        print
        print
        nprojconf = raw_input('Do you want to continue, type y or n? ') 
        if nprojconf=='y':
            clear()

            #gets various variables
            from os.path import expanduser
            home = expanduser("~")
            os.chdir(home)
            parser = ConfigParser.ConfigParser()
            parser.readfp(FakeSecHead(open('.brenda.conf')))
            #find original values
            a = parser.get('asection', 'INSTANCE_TYPE')
            b = parser.get('asection', 'BLENDER_PROJECT')
            c = parser.get('asection', 'WORK_QUEUE')
            d = parser.get('asection', 'RENDER_OUTPUT')
            e = parser.get('asection', 'DONE')
            f = parser.get('asection', 'FRAME_OR_SUBFRAME')
            g = parser.get('asection', 'TILE')
            h = parser.get('asection', 'NUMBER_INSTANCES')
            i = parser.get('asection', 'PRICE_BID')
            j = parser.get('asection', 'FILE_TYPE')
            k = parser.get('asection', 'START_FRAME')
            l = parser.get('asection', 'END_FRAME')

            #create new options
            a_nm = 'INSTANCE_TYPE='
            b_nm = 'BLENDER_PROJECT='
            c_nm = 'WORK_QUEUE='
            d_nm = 'RENDER_OUTPUT='
            e_nm = 'DONE='
            f_nm = 'FRAME_OR_SUBFRAME='
            g_nm = 'TILE='
            h_nm = 'NUMBER_INSTANCES='
            i_nm = 'PRICE_BID='
            j_nm = 'FILE_TYPE='
            k_nm = 'START_FRAME='
            l_nm = 'END_FRAME='
            z = '\n'

            projbucketname = urlparse.urlsplit(b).netloc
            projbucketpath = 's3://'+projbucketname

            #changes to s3cmd working directory
            os.chdir(ps)


            #deletes all old project files
            print
            status = os.system('python s3cmd del -r -f '+projbucketpath)
            clear()

            #deletes all old frames
            print
            status = os.system('python s3cmd del -r -f '+d)
            clear()
            print
            print "Files in project and frame buckets deleted"
            spacetime()

            #zips and moves selected file to s3 bucket
            print
            print "Zipping and uploading project file..."
            print
            os.chdir(projfilepath)
            zipper = '.zip'
            projfilenamestripped = os.path.splitext(projfilename)[0]
            zippedprojfilename = projfilenamestripped+zipper
            output = zipfile.ZipFile(zippedprojfilename, 'w')
            output.write(projfilename)
            output.close()
            os.chdir(ps)
            os.system('python s3cmd put --no-mime-magic --multipart-chunk-size-mb=5 '+projfilepath+sl+zippedprojfilename+sb+projbucketpath)
            clear()
            print
            print 'Project file uploaded'
            spacetime()

            #deletes zipped file from users pc
            os.chdir(projfilepath)
            os.remove(zippedprojfilename)

            #changes reference in config file
            home = expanduser("~")
            os.chdir(home)
            file = open(".brenda.conf", "w")
            b = projbucketpath+sl+zippedprojfilename
            newconfig = a_nm+a+z+b_nm+b+z+c_nm+c+z+d_nm+d+z+e_nm+e+z+f_nm+f+z+g_nm+g+z+h_nm+h+z+i_nm+i+z+j_nm+j+z+k_nm+k+z+l_nm+l
            file.write(newconfig)
            file.close()
            #status = os.chdir(bm)
            resetworkqueue()
            spacetime()
            break
        if nprojconf=='n':
            clear()
            break

def workq ():
    global sframe
    global eframe
    global qconf
    while True:
        print
        sframe = raw_input('Animation start frame? ')
        clear()
        print
        eframe = raw_input('Animation end frame? ')       
        clear()
        print
        print "Your animation starts at frame "+sframe,"and ends at frame "+eframe
        print
        qconf = raw_input('Are these values correct, y or n? (c to cancel and return) ')  
        if qconf=='y':
            clear()
            break
        if qconf=='c':
            clear()
            break
        if qconf=='n':
            clear()
        else:
            clear()
                
def workqinit ():    
    if qconf == 'c':
        print
        print "Request cancelled"
        return

    from os.path import expanduser
    home = expanduser("~")
    os.chdir(home)
    parser = ConfigParser.ConfigParser()
    parser.readfp(FakeSecHead(open('.brenda.conf')))
    a = parser.get('asection', 'INSTANCE_TYPE')
    b = parser.get('asection', 'BLENDER_PROJECT')
    c = parser.get('asection', 'WORK_QUEUE')
    d = parser.get('asection', 'RENDER_OUTPUT')
    e = parser.get('asection', 'DONE')
    f = parser.get('asection', 'FRAME_OR_SUBFRAME')
    g = parser.get('asection', 'TILE')
    h = parser.get('asection', 'NUMBER_INSTANCES')
    i = parser.get('asection', 'PRICE_BID')
    j = parser.get('asection', 'FILE_TYPE')
    k = parser.get('asection', 'START_FRAME')
    l = parser.get('asection', 'END_FRAME')
    #new values
    k = sframe
    l = eframe
    #create new options
    a_nm = 'INSTANCE_TYPE='
    b_nm = 'BLENDER_PROJECT='
    c_nm = 'WORK_QUEUE='
    d_nm = 'RENDER_OUTPUT='
    e_nm = 'DONE='
    f_nm = 'FRAME_OR_SUBFRAME='
    g_nm = 'TILE='
    h_nm = 'NUMBER_INSTANCES='
    i_nm = 'PRICE_BID='
    j_nm = 'FILE_TYPE='
    k_nm = 'START_FRAME='
    l_nm = 'END_FRAME='
    z = '\n'


    if f == 'frame':
        queue = py+bw+t+ft+strt+k+sb+end+l+sb+pu

    if f == 'subframe':
        queue = py+bw+t+sft+strt+k+sb+end+l+sb+xsize+g+sb+ysize+g+sb+pu
    os.chdir(bm)
    status = os.system(queue)
    print
    print
    if status == 0:
        os.chdir(home)
        #write to file
        newconfig = a_nm+a+z+b_nm+b+z+c_nm+c+z+d_nm+d+z+e_nm+e+z+f_nm+f+z+g_nm+g+z+h_nm+h+z+i_nm+i+z+j_nm+j+z+k_nm+k+z+l_nm+l
        file = open(".brenda.conf", "w")
        file.write(newconfig)
        file.close()
        os.chdir(bm)
        print 'Work queue has been built'
    if status == 1:
        print 'There was an error building work queue'
    print
    print
    exit = raw_input('Enter any key to return ')

def prices():
    spinstype = 'c1.xlarge'
    spotrequest = py+br+i+spinstype+sb+spotprice
    status = os.system(spotrequest)
    print
    spinstype = 'c3.large'
    spotrequest = py+br+i+spinstype+sb+spotprice
    status = os.system(spotrequest)
    print
    spinstype = 'c3.xlarge'
    spotrequest = py+br+i+spinstype+sb+spotprice
    status = os.system(spotrequest)
    print
    spinstype = 'c3.2xlarge'
    spotrequest = py+br+i+spinstype+sb+spotprice
    status = os.system(spotrequest)
    print
    exit = raw_input('Enter any key to return ')

def job_summary():
    from os.path import expanduser
    home = expanduser("~")
    status = os.chdir(home)
    cp = ConfigParser.SafeConfigParser()
    cp.readfp(FakeSecHead(open('.brenda.conf')))
    BLENDER_PROJECT = cp.get('asection', 'BLENDER_PROJECT')
    FILE_TYPE = cp.get('asection', 'FILE_TYPE')
    projbucketname = urlparse.urlsplit(BLENDER_PROJECT).netloc
    projname = BLENDER_PROJECT.split('/')[-1]
    projname = os.path.splitext(projname)[0]
    RENDER_OUTPUT = cp.get('asection', 'RENDER_OUTPUT')
    FRAME_OR_SUBFRAME = cp.get('asection', 'FRAME_OR_SUBFRAME')
    START_FRAME = cp.get('asection', 'START_FRAME')
    END_FRAME = cp.get('asection', 'END_FRAME')
    TILE = cp.get('asection', 'TILE')
    framebucket = urlparse.urlsplit(RENDER_OUTPUT).netloc
    reload(ami)

    intstartframe = int(START_FRAME)
    intendframe = int(END_FRAME)
    totalframe = intendframe-intstartframe+1
    if FILE_TYPE =='specifiedinfile':
        FILE_TYPE = 'as specified in uploaded .blend file'

    print "\n"
    print " %-25s %-15s" % ('AMI used',ami.AMI_ID)
    print
    print " %-25s %-15s" % ('Project name',projname)
    print
    print " %-25s %-15s" % ('Frame or sub-frame',FRAME_OR_SUBFRAME)
    if FRAME_OR_SUBFRAME == 'subframe':
        x = 'x'
        print
        print " %-25s %-15s" % ('Tile grid',TILE+x+TILE)
    print
    print " %-25s %-15s" % ('Frame format',FILE_TYPE)
    print 
    print " %-25s %-15s" % ('Start frame',START_FRAME)
    print
    print " %-25s %-15s" % ('End frame',END_FRAME)
    print
    print " %-25s %-15s" % ('Total frames',totalframe)
    print "\n\n"
    exit = raw_input('Enter any key to return ')
    status = os.chdir(bm)


def instance():
    global amount
    global price
    global iconf
    while True:
        print
        print "a = c1.xlarge"
        print "b = c3.large"
        print "c = c3.xlarge"
        print "d = c3.2xlarge"
        print
        inst = raw_input('Which instance would you like to use? ')
        clear()
        print
        amount = raw_input('How many instances would you like to initiate? ')
        clear()
        print
        price = raw_input('How much would you like to bid per instance hour? ')
        clear()
        global type
        while True:
            if inst == 'a':
                type = 'c1.xlarge'
                break
            if inst == 'b':
                type = 'c3.large'
                break
            if inst == 'c':
                type = 'c3.xlarge'
                break
            if inst == 'd':
                type = 'c3.2xlarge'
                break
        print
        print "You are bidding for "+amount,"X"+sb+type,"at a cost of $ "+price,"per instance."
        print
        amountD = Decimal(amount)
        priceD = Decimal(price)
        math = (amountD*priceD)
        print 'This will cost you $',math, 'per hour'
        print
        iconf = raw_input('Are these values correct, y or n? (c to cancel and return) ')  
        if iconf=='y':
            clear()
            break
        if iconf=='c':
            clear()
            break
        if iconf =='n':
            clear()

def instanceinit ():
    if iconf == 'c':
        print
        print "Request cancelled"
        return   
    instrequest = py+br+i+type+sb+n+amount+sb+p+price+sb+spot
    status = os.system(instrequest)
    print
    print
    if status == 0:
        print 'Instance/s have been initiated'
    if status == 1:
        print 'There was an error initiating Instances'
    print
    print
    exit = raw_input('Enter any key to return ')
        
def setupmenu ():
    while True:
        clear()
        status = os.chdir(bm)
        setupmenuoptions()
        setuptask = raw_input('Which task would you like to perform? ')    
        if setuptask=='m':
            clear()
            break
        if setuptask=='u':  
            clear()
            amis()
        if setuptask=='n':
            clear()
            nproj()
        if setuptask=='f':  
            clear()
            frames()
        if setuptask=='b':  
            clear()
            workq()
            workqinit()
        if setuptask=='j':
            clear()
            job_summary()
        if setuptask=='p':  
            clear()
            prices()

        if setuptask=='i':  
            clear()
            instance()
            instanceinit()

def monmenuoptions ():
    print 
    print "m = Go to main menu"
    print
    print
    print "w = Work queue status"
    print "r = Run status"
    print "u = Uptime of instances"
    print "t = Tail log from instances"
    print "f = Farm performance"
    print "c = Instance task (frame) count"
    print "p = Prune instances"
    print
    print

def monmenu ():
    while True:
        clear()
        status = os.chdir(bm)
        monmenuoptions()
        montask = raw_input('Which task would you like to perform? ')    
        if montask=='m':
            clear()
            break
        if montask=='w':  
            clear()
            print
            status = os.system(py+bw+st)      
            print
            print
            exit = raw_input('Enter any key to return ')
        if montask=='r':  
            clear()
            print
            os.system(py+br+st)     
            print
            print
            exit = raw_input('Enter any key to return ')
        if montask=='u':           
            clear()
            print
            os.system(py+bt+sh+ut)      
            print
            print
            exit = raw_input('Enter any key to return ')
        if montask=='t':           
            clear()
            print
            os.system(py+bt+sh+tl)      
            print
            print
            exit = raw_input('Enter any key to return ')
        if montask=='f':           
            clear()
            print
            os.system(py+bt+pf)    
            print  
            print
            exit = raw_input('Enter any key to return ')
        if montask=='c':           
            clear()
            print
            os.system(py+bt+sh+tc)      
            print
            print
            exit = raw_input('Enter any key to return ')
        if montask=='p':           
            clear()
            while True:
                print
                print 'Would you like to do a dry run?'
                print
                print 'y = Yes'
                print 'n = No'
                print
                dry = raw_input('Enter your choice ')
                if dry==('y'):
                    dry = 'y'
                    break
                if dry==('n'):
                    dry = 'n'
                    break
            clear()
            while True:
                print
                print 'Would you like to only prune instances close to transitioning'
                print 'to their next billable hour?'
                print
                print 'y = Yes'
                print 'n = No'
                print
                trans = raw_input('Enter your choice ')
                if trans=='y':
                    clear()
                    print
                    uptime = raw_input('What should the minimum uptime (in minutes) of pruned instances be? ')
                    clear()
                    print
                    inprunet = raw_input('How many instances would you like to reduce the farm to? ')
                    clear()
                    if dry =='y':
                        close = py+bt+t+dflag+smlt+uptime+sb+pru+inprunet
                    if dry =='n':
                        close = py+bt+t+smlt+uptime+sb+pru+inprunet
                    os.system(close)
                    print
                    exit = raw_input('Enter any key to return ')
                    clear()
                    break                
                if trans=='n':
                    clear()
                    print
                    inprune = raw_input('How many instances would you like to reduce the farm to? ')
                    clear()
                    if dry =='y':
                        close2 = py+bt+t+dflag+pru+inprune
                    if dry =='n':
                        close2 = py+bt+t+pru+inprune
                    os.system(close2)
                    print
                    exit = raw_input('Enter any key to return ')
                    clear()
                    break

def downmenuoptions ():
    print 
    print "m = Go to main menu"
    print
    print
    print "o = One time download to local folder"
    print "r = Regular download to local folder (to avoid a large final download)"
    print
    print

class FakeSecHead(object):
    def __init__(self, fp):
        self.fp = fp
        self.sechead = '[asection]\n'

    def readline(self):
        if self.sechead:
            try: 
                return self.sechead
            finally: 
                self.sechead = None
        else: 
            return self.fp.readline()

def downmenu ():
    while True:
        clear()
        downmenuoptions()
        downtask = raw_input('which task would you like to perform? ')
        if downtask =='m':
            clear()
            break
        if downtask =='o': 
            clear()
            root = Tk()
            root.withdraw()
            print
            print "Select a folder to download frames to..."
            time.sleep(1)
            dir = askdirectory(parent=root, title='Select a folder to download frames to')
            root.destroy()
            clear()
            print
            print "Downloading frames..."
            print  
            from os.path import expanduser
            home = expanduser("~")
            status = os.chdir(home)
            cp = ConfigParser.SafeConfigParser()
            cp.readfp(FakeSecHead(open('.brenda.conf')))
            RENDER_OUTPUT = cp.get('asection', 'RENDER_OUTPUT')      
            status = os.chdir(ps)
            status = os.system('python s3cmd get -r --skip-existing '+RENDER_OUTPUT+sb+dir)
            clear()
            print
            print "Frames have been downloaded"
            print
            print
            exit = raw_input('Enter any key to return ')
            status = os.chdir(bm)
        if downtask =='r': 
            clear()
            print
            tinterval = raw_input('Time interval between checking for new frames and downloading (minutes)? ')
            t = int(tinterval)*60
            clear()
            root = Tk()
            root.withdraw()
            print
            print "Select a folder to download frames to..."
            time.sleep(1)
            dir = askdirectory(parent=root, title='Select a folder to download frames to')
            root.destroy()
            clear()
            from os.path import expanduser
            home = expanduser("~")
            status = os.chdir(home)
            cp = ConfigParser.SafeConfigParser()
            cp.readfp(FakeSecHead(open('.brenda.conf')))
            RENDER_OUTPUT = cp.get('asection', 'RENDER_OUTPUT')
            try:
                while True:
                    print
                    print "Checking for new frames every "+tinterval,"minutes"
                    print
                    print """Press "control-c" to stop regular download and return"""
                    print
                    status = os.chdir(ps)
                    status = os.system('python s3cmd get -r --skip-existing '+RENDER_OUTPUT+sb+dir)
                    status = os.chdir(bm)
                    clear()
                    print
                    print "Checking for new frames every "+tinterval,"minutes"
                    print
                    print """Press "control-c" to stop regular download and return"""
                    print
                    time.sleep(t)
                    clear()

            except KeyboardInterrupt:
                clear()

def cancelmenuoptions ():
    print 
    print "m = Go to main menu"
    print
    print
    print "r = Reset work queue"
    print "s = Stop all running instances"
    print "c = Cancel pending spot requests"
    print
    print

def cancelmenu ():
    while True:
        clear()
        status = os.chdir(bm)
        cancelmenuoptions()
        canceltask = raw_input('Which task would you like to perform? ')    
        if canceltask=='m':
            clear()           
            break  
        if canceltask=='r':  
            clear()
            resetworkqueue()
            print
            print
            exit = raw_input('Enter any key to return ')


        if canceltask=='s':  
            clear()
            print
            status = os.system(py+br+t+sp)
            if status==0:
                print
                print
                print "Instances have been stopped"
            if status==1:
                print
                print
                print
                print "There was a problem, please try an alternative method" 
            print
            print
            exit = raw_input('Enter any key to return ')
        if canceltask=='c':  
            clear()
            print
            status = os.system(py+br+ca)
            if status==0:
                print
                print
                print "Pending spot requests have been cancelled"
            if status==1:
                print
                print
                print
                print "There was a problem, please try an alternative method" 
            print
            print
            exit = raw_input('Enter any key to return ')

#This recreates the original "s3cmd.ini" file by making a duplicate of the ".s3cmd" file created by win_brenda_installer, renaming it to "s3cmd.ini" and moving it back
def inidup ():
    from os.path import expanduser
    home = expanduser("~")
    s3cmd_there = os.path.isfile(home+ap+ini)
    if s3cmd_there == False:
        clear()
        shutil.copyfile(home+sl+scf, home+ap+scf)
        os.rename(home+ap+scf, home+ap+ini)

#This changes a line in the "tool.py" file as new Ubuntu AMIs only let you ssh in as "ubuntu" and not "tool" whereas old Ubuntu AMIs let you log in as both
def toolchange ():
    x = 'tool.py'
    with open(bm+sl+brenda+sl+x, 'r') as file:
        data = file.readlines()
    data[73] = """                user = utils.get_opt(opts.user, conf, 'AWS_USER', default='ubuntu')\n"""
    with open(bm+sl+brenda+sl+x, 'w') as file:
        file.writelines( data )

#This checks the version number and shows a notification if there is a newer version up on github
def vercheck ():
    clear()
    urllib.urlretrieve ("http://www.thegreyroompost.com/win_brenda/win_brenda.ini", "win_brenda.ini")
    parser = SafeConfigParser()
    parser.read('win_brenda.ini')
    ghver = parser.get('versions', 'ghver')
    os.remove('win_brenda.ini')
    ghver = int(ghver)
    if ghver > thisver:
        print
        print
        print "UPDATED VERSION AVAILABLE"
        print 
        print "Check github"
        print 
        spacetime()

#This checks frame and subframe options in .conf file
def confadd ():
    from os.path import expanduser
    home = expanduser("~")
    os.chdir(home)
    parser = ConfigParser.ConfigParser()
    parser.readfp(FakeSecHead(open('.brenda.conf')))
    fos = parser.has_option('asection', 'FRAME_OR_SUBFRAME')
    if fos == False:
        #find original values
        a = parser.get('asection', 'INSTANCE_TYPE')
        b = parser.get('asection', 'BLENDER_PROJECT')
        c = parser.get('asection', 'WORK_QUEUE')
        d = parser.get('asection', 'RENDER_OUTPUT')
        e = parser.get('asection', 'DONE')
        #new values
        f = 'frame'
        g = 'non'
        h = '0'
        i = '0.00'
        j = 'png'
        k = '0'
        l = '0'
        #create new options
        a_nm = 'INSTANCE_TYPE='
        b_nm = 'BLENDER_PROJECT='
        c_nm = 'WORK_QUEUE='
        d_nm = 'RENDER_OUTPUT='
        e_nm = 'DONE='
        f_nm = 'FRAME_OR_SUBFRAME='
        g_nm = 'TILE='
        h_nm = 'NUMBER_INSTANCES='
        i_nm = 'PRICE_BID='
        j_nm = 'FILE_TYPE='
        k_nm = 'START_FRAME='
        l_nm = 'END_FRAME='
        z = '\n'
        #write to file
        newconfig = a_nm+a+z+b_nm+b+z+c_nm+c+z+d_nm+d+z+e_nm+e+z+f_nm+f+z+g_nm+g+z+h_nm+h+z+i_nm+i+z+j_nm+j+z+k_nm+k+z+l_nm+l
        file = open(".brenda.conf", "w")
        file.write(newconfig)
        file.close()

def frames ():
    while True:
        clear()
        print
        print "m = Go to main menu"
        print
        print
        print 'w = Whole frames'
        print 's = Sub-frames tiles'
        print 'f = File format '
        print
        print
        conf = read_conf_values()
        framechoice = raw_input('Choose frame option: ')
        if framechoice == 'm':
            break

        if framechoice == 'w':
            clear()
            #new values
            f = 'frame'
            g = 'non'
            #write to file
            newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+f+conf.z+conf.g_nm+g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+conf.j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
            confwrite(newconfig)
            print
            print 'Changed to whole frame rendering'
            spacetime()


        if framechoice == 's':
            while True:
                clear()
                print
                print 'a = 64 8x8'
                print 'b = 16 4x4'
                print 'c = 4  2x2'
                print
                print
                tilechoice = raw_input('How many tiles will frames be split into? ')
                clear()              
                if tilechoice =='a':
                    #new value
                    f = 'subframe'
                    g = '8'
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+f+conf.z+conf.g_nm+g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+conf.j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    print
                    print 'Changed to sub-frame rendering'
                    spacetime()
                    break

                if tilechoice =='b':
                    #new value
                    f = 'subframe'
                    g = '4'
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+f+conf.z+conf.g_nm+g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+conf.j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    print
                    print 'Changed to sub-frame rendering'
                    spacetime()
                    break
                if tilechoice =='c':
                    #new value
                    f = 'subframe'
                    g = '2'
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+f+conf.z+conf.g_nm+g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+conf.j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    print
                    print 'Changed to sub-frame rendering'
                    spacetime()
                    break

        if framechoice == 'f':
            while True:
                clear()
                print
                print 'p = PNG'
                print 'e = EXR'
                print 'j = JPEG'
                print 't = TIFF'
                print 'f = Format specified in uploaded .blend file'
                print
                print
                formatchoice = raw_input('Enter the file format you wish frames to be rendered in? ')
                if formatchoice=='p':
                    #new values
                    j = 'PNG'
                    clear()
                    frametemplateformat(sb+ff+sb+j+sb)
                    subframetemplateformat(sb+ff+sb+j+sb)
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+conf.f+conf.z+conf.g_nm+conf.g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    clear()
                    print
                    print 'Changed frame format to '+j
                    spacetime()
                    break

                if formatchoice=='e':
                    j = 'EXR'
                    clear()
                    frametemplateformat(sb+ff+sb+j+sb)
                    subframetemplateformat(sb+ff+sb+j+sb)
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+conf.f+conf.z+conf.g_nm+conf.g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    clear()
                    print
                    print 'Changed frame format to '+j
                    spacetime()
                    break

                if formatchoice=='j':
                    j = 'JPEG'
                    clear()
                    frametemplateformat(sb+ff+sb+j+sb)
                    subframetemplateformat(sb+ff+sb+j+sb)                
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+conf.f+conf.z+conf.g_nm+conf.g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    clear()
                    print
                    print 'Changed frame format to '+j
                    spacetime()
                    break

                if formatchoice=='t':
                    j = 'TIFF'
                    clear()
                    frametemplateformat(sb+ff+sb+j+sb)
                    subframetemplateformat(sb+ff+sb+j+sb)
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+conf.f+conf.z+conf.g_nm+conf.g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    clear()
                    print
                    print 'Changed frame format to '+j
                    spacetime()
                    break

                if formatchoice=='f':
                    frametemplateformat(sb)
                    subframetemplateformat(sb)
                    #new values
                    j = 'specifiedinfile'
                    #write to file
                    newconfig = conf.a_nm+conf.a+conf.z+conf.b_nm+conf.b+conf.z+conf.c_nm+conf.c+conf.z+conf.d_nm+conf.d+conf.z+conf.e_nm+conf.e+conf.z+conf.f_nm+conf.f+conf.z+conf.g_nm+conf.g+conf.z+conf.h_nm+conf.h+conf.z+conf.i_nm+conf.i+conf.z+conf.j_nm+j+conf.z+conf.k_nm+conf.k+conf.z+conf.l_nm+conf.l
                    confwrite(newconfig)
                    clear()
                    print
                    print 'Changed to format specified in uploaded .blend file'
                    spacetime()
                    break


def frametemplateformat(newformat):
    os.chdir(bm)
    fpart = 'blender -b *.blend'
    lpart = '-o $OUTDIR/frame_###### -s $START -e $END -j $STEP -t 0 -a'
    file = open("frame-template", "w")
    file.write(fpart+newformat+lpart)
    file.close()

def subframetemplateformat(newformat):
    os.chdir(bm)
    fpart = """cat >subframe.py <<EOF
import bpy
bpy.context.scene.render.border_min_x = $SF_MIN_X
bpy.context.scene.render.border_max_x = $SF_MAX_X
bpy.context.scene.render.border_min_y = $SF_MIN_Y
bpy.context.scene.render.border_max_y = $SF_MAX_Y
bpy.context.scene.render.use_border = True
EOF
blender -b *.blend -P subframe.py"""
    lpart = """-o $OUTDIR/frame_######_X-$SF_MIN_X-$SF_MAX_X-Y-$SF_MIN_Y-$SF_MAX_Y -s $START -e $END -j $STEP -t 0 -a"""
    file = open("subframe-template", "w")
    file.write(fpart+newformat+lpart)
    file.close()


class read_conf_values():
    from os.path import expanduser
    home = expanduser("~")
    os.chdir(home)
    parser = ConfigParser.ConfigParser()
    parser.readfp(FakeSecHead(open('.brenda.conf')))
    a = parser.get('asection', 'INSTANCE_TYPE')
    b = parser.get('asection', 'BLENDER_PROJECT')
    c = parser.get('asection', 'WORK_QUEUE')
    d = parser.get('asection', 'RENDER_OUTPUT')
    e = parser.get('asection', 'DONE')
    f = parser.get('asection', 'FRAME_OR_SUBFRAME')
    g = parser.get('asection', 'TILE')
    h = parser.get('asection', 'NUMBER_INSTANCES')
    i = parser.get('asection', 'PRICE_BID')
    j = parser.get('asection', 'FILE_TYPE')
    k = parser.get('asection', 'START_FRAME')
    l = parser.get('asection', 'END_FRAME')
    #create new options
    a_nm = 'INSTANCE_TYPE='
    b_nm = 'BLENDER_PROJECT='
    c_nm = 'WORK_QUEUE='
    d_nm = 'RENDER_OUTPUT='
    e_nm = 'DONE='
    f_nm = 'FRAME_OR_SUBFRAME='
    g_nm = 'TILE='
    h_nm = 'NUMBER_INSTANCES='
    i_nm = 'PRICE_BID='
    j_nm = 'FILE_TYPE='
    k_nm = 'START_FRAME='
    l_nm = 'END_FRAME='
    z = '\n'
    os.chdir(bm)


def confwrite(newconfig):
    from os.path import expanduser
    home = expanduser("~")
    os.chdir(home)
    file = open(".brenda.conf", "w")
    file.write(newconfig)
    file.close()
    os.chdir(bm)



def resetworkqueue():
    os.chdir(bm)
    status = os.system(py+bw+rs)
    if status==0:
        from os.path import expanduser
        home = expanduser("~")
        os.chdir(home)
        parser = ConfigParser.ConfigParser()
        parser.readfp(FakeSecHead(open('.brenda.conf')))
        #find original values
        a = parser.get('asection', 'INSTANCE_TYPE')
        b = parser.get('asection', 'BLENDER_PROJECT')
        c = parser.get('asection', 'WORK_QUEUE')
        d = parser.get('asection', 'RENDER_OUTPUT')
        e = parser.get('asection', 'DONE')
        f = parser.get('asection', 'FRAME_OR_SUBFRAME')
        g = parser.get('asection', 'TILE')
        h = parser.get('asection', 'NUMBER_INSTANCES')
        i = parser.get('asection', 'PRICE_BID')
        j = parser.get('asection', 'FILE_TYPE')
        k = parser.get('asection', 'START_FRAME')
        l = parser.get('asection', 'END_FRAME')
        #new values
        k = '0'
        l = '0'
        #create new options
        a_nm = 'INSTANCE_TYPE='
        b_nm = 'BLENDER_PROJECT='
        c_nm = 'WORK_QUEUE='
        d_nm = 'RENDER_OUTPUT='
        e_nm = 'DONE='
        f_nm = 'FRAME_OR_SUBFRAME='
        g_nm = 'TILE='
        h_nm = 'NUMBER_INSTANCES='
        i_nm = 'PRICE_BID='
        j_nm = 'FILE_TYPE='
        k_nm = 'START_FRAME='
        l_nm = 'END_FRAME='
        z = '\n'
        #write to file
        newconfig = a_nm+a+z+b_nm+b+z+c_nm+c+z+d_nm+d+z+e_nm+e+z+f_nm+f+z+g_nm+g+z+h_nm+h+z+i_nm+i+z+j_nm+j+z+k_nm+k+z+l_nm+l
        file = open(".brenda.conf", "w")
        file.write(newconfig)
        file.close()
        print
        print "Work queue has been reset"
    if status==1:
        print
        print
        print
        print "There was a problem resetting work queue, please try waiting 60 seconds"
    os.chdir(bm)




def subframecreate ():
    status = os.chdir(bm)
    subframe_template_there = os.path.isfile('subframe-template')
    if subframe_template_there == False:
        file = open("subframe-template", "w")
        file.write("""cat >subframe.py <<EOF
import bpy
bpy.context.scene.render.border_min_x = $SF_MIN_X
bpy.context.scene.render.border_max_x = $SF_MAX_X
bpy.context.scene.render.border_min_y = $SF_MIN_Y
bpy.context.scene.render.border_max_y = $SF_MAX_Y
bpy.context.scene.render.use_border = True
EOF
blender -b *.blend -P subframe.py -F PNG -o $OUTDIR/frame_######_X-$SF_MIN_X-$SF_MAX_X-Y-$SF_MIN_Y-$SF_MAX_Y -s $START -e $END -j $STEP -t 0 -a""")
        file.close()




vercheck()
subframecreate()
toolchange()
inidup()
confadd()
mainmenu()
