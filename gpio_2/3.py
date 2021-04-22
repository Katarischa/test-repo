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
GPIO.setup(4, GPIO.IN) 


bit_depth = 8
GPIO.output(17, 1)

try:
    while True:
        first = 0
        end = 255
        mid = 255 // 2


        while True:
            lightNumber(mid)
            time.sleep(0.1)
            if GPIO.input(4) == 1:
                first = mid
            else:
                end = mid
            mid = (end + first) // 2
            if mid == first or mid == end:
                print('Digital value:',mid , 'Analog value:', round(mid*3.241/255, 3), 'V')
                break
finally:
    lightNumber(0)
    GPIO.cleanup()
