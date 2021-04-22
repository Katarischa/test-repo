
import RPi.GPIO as GPIO 
import time 



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




GPIO.setmode(GPIO.BCM)
chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
chan_list.reverse()

GPIO.setup(chan_list, GPIO.OUT)
GPIO.setup(17, GPIO.OUT) 

bit_depth = 8
GPIO.output(17, 1)

print("Enter value(-1 to exit)>")    
while True:
    try:
        value = int(input())
        if value >-1:
            lightNumber(value)
            print(value*3.241/255)
        elif value == -1:
            lightNumber(0)
            GPIO.cleanup()
            exit()
    except ValueError:
        print("value must be integer")
