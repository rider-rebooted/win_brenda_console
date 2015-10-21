import time
import os
from decimal import *

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

status = os.chdir(bm)

def mainmenuoptions ():
    print
    print
    print
    print
    print "s = Setting up your farm"
    print "m = Managing your farm"
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
    print "b = Build work queue"
    print "p = Price of instance"
    print "i = Initiate instances"
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
        if qconf=='n':
            clear()
                
def workqinit ():    
    if qconf == 'c':
        print
        print "Request cancelled"
        return
    queue = py+bw+t+ft+s+sframe+sb+e+eframe+sb+pu
    status = os.system(queue)
    print
    exit = raw_input('Enter any key to exit ')

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
    exit = raw_input('Enter any key to exit ')


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
    print
    exit = raw_input('Enter any key to exit ')
        
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
            status = os.system(py+bw+st)      
            print
            exit = raw_input('Enter any key to exit ')
        if montask=='r':  
            clear()
            os.system(py+br+st)     
            print
            exit = raw_input('Enter any key to exit ')
        if montask=='u':           
            clear()
            os.system(py+bt+sh+ut)      
            print
            exit = raw_input('Enter any key to exit ')
        if montask=='t':           
            clear()
            os.system(py+bt+sh+tl)      
            print
            exit = raw_input('Enter any key to exit ')
        if montask=='f':           
            clear()
            os.system(py+bt+pf)      
            print
            exit = raw_input('Enter any key to exit ')
        if montask=='c':           
            clear()
            os.system(py+bt+sh+tc)      
            print
            exit = raw_input('Enter any key to exit ')
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
                    exit = raw_input('Enter any key to exit ')
                    clear()
                    break                
                if trans=='n':
                    clear()
                    print
                    inprune = raw_input('How many instances would you reduce the farm to? ')
                    clear()
                    if dry =='y':
                        close2 = py+bt+t+dflag+pru+inprune
                    if dry =='n':
                        close2 = py+bt+t+pru+inprune
                    os.system(close2)
                    print
                    exit = raw_input('Enter any key to exit ')
                    clear()
                    break

def cancelmenuoptions ():
    print 
    print "m = Go to main menu"
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
            print
            exit = raw_input('Enter any key to exit ')
        if canceltask=='s':  
            clear()   
            status = os.system(py+br+t+sp)
            print
            exit = raw_input('Enter any key to exit ')
        if canceltask=='c':  
            clear()   
            status = os.system(py+br+ca)
            print
            exit = raw_input('Enter any key to exit ')
                
mainmenu()
