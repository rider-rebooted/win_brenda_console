import time
import os

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

rs = 'reset'
t = '-T '
sp = 'stop'
ca = 'cancel'



def mainmenuoptions ():
    print
    print
    print
    print
    print "s = Setting up your farm"
    print "m = Monitoring your farm"
    print "c = Canceling and resetting your farm"
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
        if submen =='c':           
            cancelmenu()
             


def setupmenuoptions ():
    print 
    print "m = Go to main menu"
    print
    print
    print "b = build work queue"
    print "i = initiate instances"
    print
    print
    




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
        qconf = raw_input('Are these values correct, y or n? (c to cancel) ')  
        if qconf=='y':
            clear()
            break
        if qconf=='c':
            clear()
            break
        if fconf=='n':
            clear()
                
def workqinit ():    
    if qconf == 'c':
        print
        print "Request cancelled"
        return
    queue = py+bw+t+ft+s+sframe+sb+e+eframe+sb+pu
    status = os.system(queue)
    spacetime()

def instance():
    global amount
    global price
    global iconf
    while True:
        print
        print "a = c3.large"
        print "b = c3.2xlarge"
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
                type = 'c3.large'
                break
            if inst == 'b':
                type = 'c3.2xlarge'
                break
        print
        print "You are bidding for "+amount,"X"+sb+type,"at a cost of $"+price," per instance."
        print
        iconf = raw_input('Are these values correct, y or n? (c to cancel) ')  
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
    spacetime()
        
        


def setupmenu ():
    while True:
        clear()
        setupmenuoptions()
        setuptask = raw_input('Which task would you like to perform? ')    
        if setuptask=='m':
            clear()
            break
        if setuptask=='b':  
            clear()
            workq()
            workqinit()
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
    print "u = Instance uptime"
    print "t = Instance tail log"
    print "p = Render farm performance"
    print "f = Instance task (frame) count"
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
            status = os.system(py+bw+st)      
            spacetime()
        if montask=='r':  
            clear()
            os.system(py+br+st)     
            spacetime()
        if montask=='u':           
            clear()
            os.system(py+bt+sh+ut)      
            spacetime()
        if montask=='t':           
            clear()
            os.system(py+bt+sh+tl)      
            spacetime()
        if montask=='p':           
            clear()
            os.system(py+bt+pf)      
            spacetime()
        if montask=='f':           
            clear()
            os.system(py+bt+sh+tc)      
            spacetime()


def cancelmenuoptions ():
    print 
    print "m = Go to main menu"
    print
    print
    print "r = Reset work queue"
    print "s = Stop all running instances"
    print "c = Cancel pending spot requests"
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
            status = os.system(py+bw+rs)
            print "Work queue has been reset"      
            spacetime()
        if canceltask=='s':  
            clear()   
            status = os.system(py+br+t+sp)
            spacetime()
        if canceltask=='c':  
            clear()   
            status = os.system(py+br+ca)
            spacetime()
                
mainmenu()



    
    
