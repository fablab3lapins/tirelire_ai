mport RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


bt = 2


GPIO.setup(bt, GPIO.IN)


a1 = 24
a2 = 25
b1 = 8
b2 = 7
delay = 0.005

GPIO.setup(a1, GPIO.OUT)
GPIO.setup(a2, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)


def arriere():
    setp(1,0,0,0)
    setp(1,1,0,0)
    setp(0,1,0,0)
    setp(0,1,1,0)
    setp(0,0,1,0)
    setp(0,0,1,1)
    setp(0,0,0,1)
    setp(1,0,0,1)
    
   


def avant():
    setp(1,0,0,1)
    setp(0,0,0,1)
    setp(0,0,1,1)
    setp(0,0,1,0)
    setp(0,1,1,0)
    setp(0,1,0,0)
    setp(1,1,0,0)
    setp(1,0,0,0)
    


def setp(pin1, pin2, pin3, pin4):
    GPIO.output(a1, pin1)
    GPIO.output(a2, pin2)
    GPIO.output(b1, pin3)
    GPIO.output(b2, pin4)
    time.sleep(delay)



v=0

while (v==0):
    print("avant")
    for i in range(5120):
        avant()
        if (GPIO.input(bt) == False):
            v+=1
            #break
    time.sleep(1)
    print("arriere")
    for i in range(512):
        arriere()
        if (GPIO.input(bt) == False):
            v+=1
            break

print("uit's done")

for i in range(110):
    arriere()























        
