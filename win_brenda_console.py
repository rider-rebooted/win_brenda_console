import time
import os
from decimal import *
import shutil
from Tkinter import *
from tkFileDialog import *
import ConfigParser
import urlparse
import zipfile

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
s = '-s '
e = '-e '
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

status = os.chdir(bm)




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
    print "n = New project"
    print "b = Build work queue"
    print "p = Price of instance"
    print "i = Initiate instances"
    print
    print

def ami ():
    while True:
        clear()
        print
        ami = raw_input('Enter the new public AMI you wish to use (e.g. "ami-0529086c") ')
        clear()
        print
        print 'Your new AMI will be changed to '+q+ami+q
        print
        print
        amiconf = raw_input('Do you want to continue, type y or n? ') 
        if amiconf=='y':
            clear()
            print
            print "Updating AMI..."
            status = os.chdir(bm+sl+brenda)
            file = open("ami.py", "w")
            w = """# An AMI that contains Blender and Brenda (may be None)
AMI_ID="""
            file.write(w+q+ami+q)
            file.close()
            spacetime ()
            print
            print "Done"
            spacetime()
            status = os.chdir(bm)
            break
        if amiconf=='n':
            clear()
            break


def nproj ():
    while True:
        print
        print "Select your Blender project file (should not be zipped and must be packed)"
        time.sleep(1)
        root = Tk()
        root.withdraw()
        projfile = askopenfilename(parent=root, title='select your zipped and packed Blender project file')
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
        print "3. update the brenda.conf file"
        print
        print
        nprojconf = raw_input('Do you want to continue, type y or n? ') 
        if nprojconf=='y':
            clear()

            #gets path of project file in s3 bucket
            from os.path import expanduser
            home = expanduser("~")
            status = os.chdir(home)
            cp = ConfigParser.SafeConfigParser()
            cp.readfp(FakeSecHead(open('.brenda.conf')))
            BLENDER_PROJECT = cp.get('asection', 'BLENDER_PROJECT')
            projbucketname = urlparse.urlsplit(BLENDER_PROJECT).netloc
            projbucketpath = 's3://'+projbucketname


            #gets sqs work queue name
            from os.path import expanduser
            home = expanduser("~")
            status = os.chdir(home)
            cp = ConfigParser.SafeConfigParser()
            cp.readfp(FakeSecHead(open('.brenda.conf')))
            workqpath = cp.get('asection', 'WORK_QUEUE')

            #gets frame bucket path
            from os.path import expanduser
            home = expanduser("~")
            status = os.chdir(home)
            cp = ConfigParser.SafeConfigParser()
            cp.readfp(FakeSecHead(open('.brenda.conf')))
            framebucketpath = cp.get('asection', 'RENDER_OUTPUT')


            #changes to s3cmd working directory
            status = os.chdir(ps)


            #deletes all old project files
            print
            status = os.system('python s3cmd del -r -f '+projbucketpath)
            clear()

            #deletes all old frames
            print
            status = os.system('python s3cmd del -r -f '+framebucketpath)
            clear()
            print
            print "Deleted"
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
            spacetime()

            #deletes zipped file from users pc
            os.chdir(projfilepath)
            os.remove(zippedprojfilename)

            #changes reference in config file
            home = expanduser("~")
            status = os.chdir(home)
            file = open(".brenda.conf", "w")
            print
            print "Updating Brenda configuration file..."
            u = """INSTANCE_TYPE=c3.large
BLENDER_PROJECT=s3://"""
            v = '/'
            w = """
WORK_QUEUE="""
            x = """
RENDER_OUTPUT="""
            y = """
DONE=shutdown
\n"""
            file.write(u+projbucketname+v+zippedprojfilename+w+workqpath+x+framebucketpath+y)
            file.close()
            status = os.chdir(bm)
            spacetime ()
            print
            print "Done"
            spacetime()
            status = os.chdir(bm)
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
    queue = py+bw+t+ft+s+sframe+sb+e+eframe+sb+pu
    status = os.system(queue)
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
    exit = raw_input('Enter any key to return ')
        
def setupmenu ():
    while True:
        clear()
        setupmenuoptions()
        setuptask = raw_input('Which task would you like to perform? ')    
        if setuptask=='m':
            clear()
            break
        if setuptask=='u':  
            clear()
            ami()
        if setuptask=='n':  
            clear()
            nproj()
        if setuptask=='b':  
            clear()
            workq()
            workqinit()

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
            print "Select a folder to download frames to"
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
            print "Select a folder to download frames to"
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
        cancelmenuoptions()
        canceltask = raw_input('Which task would you like to perform? ')    
        if canceltask=='m':
            clear()           
            break  
        if canceltask=='r':  
            clear()
            print
            status = os.system(py+bw+rs)
            if status==0:
                print
                print "Work queue has been reset"
            if status==1:
                print
                print
                print
                print "There was a problem, please try waiting 60 seconds or use an alternative method" 
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
                print "There was a problem, please try waiting 60 seconds or use an alternative method" 
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
                print "There was a problem, please try waiting 60 seconds or use an alternative method" 
            print
            print
            exit = raw_input('Enter any key to return ')

def inidup ():
    from os.path import expanduser
    home = expanduser("~")
    there = os.path.isfile(home+ap+ini)
    if there == False:
        clear()
        print
        print """Recreating the original "s3cmd.ini" file..."""
        print
        print "(required for working with buckets)"
        spacetime()
        shutil.copyfile(home+sl+scf, home+ap+scf)
        status = os.rename(home+ap+scf, home+ap+ini)

inidup()
mainmenu()
