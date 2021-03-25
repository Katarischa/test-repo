import RPi.GPIO as GPIO 
import time 


GPIO.setmode(GPIO.BCM)
chan_list = [21, 20, 16, 12, 7, 8, 25, 24]
chan_list.reverse()

GPIO.setup(chan_list, GPIO.OUT)
 

bit_depth = 8



def lightUp(ledNumber, period):
    GPIO.output(ledNumber, 1)
    time.sleep(period)
    GPIO.output(ledNumber, 0)


def blink(ledNumber, blinkCount, blinkPeriod):
    for i in range(blinkCount):
        GPIO.output(ledNumber, 1)
        time.sleep(blinkPeriod)
        GPIO.output(ledNumber, 0)
        time.sleep(blinkPeriod)

def runningLight(count, period):
    for i in range(count):
        for j in chan_list:
            GPIO.output(j, 1)
            time.sleep(period)
            GPIO.output(j, 0)


def runningDark (count, period):
    GPIO.output(chan_list,1)
    for i in range(count):
        for j in chan_list:
            GPIO.output(j, 0)
            time.sleep(period)
            GPIO.output(j, 1)



def decToBinList(decNumber):
    N = bit_depth - 1
    p = 0
    x = []
    while N > 0:
        p = int(decNumber/2**N)
        if p == 1:
            x.append(1)
            decNumber -= 2**N
        else:
            x.append(0)
        N -= 1
    x.append(decNumber)
    return x

def lightNumber(decNumber):
    x = decToBinList(decNumber)
    x.reverse()
    GPIO.output(chan_list, x)


#n = int(input("Enter LED number> "))
#period = int(input("Enter period> "))
#blink_count = int(input("Enter count>"))
#number = int(input("Enter decMumber>"))

#lightUp(chan_list[5], 2)
#blink(chan_list[3],3,0.2)
#runningDark(2,0.1)
decToBinList(3)
lightNumber(4)
time.sleep(5)
#runningDark(blink_count,period)
GPIO.output(chan_list,0)
GPIO.cleanup()