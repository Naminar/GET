import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = 22
val = 0
valt = 3.3

GPIO.setup(dac, GPIO.OUT)

p = GPIO.PWM(dac, 50)

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:  
    while True:
            arg = input("enter your period\n")
            if(int(arg) < 0 or int(arg) > 255):
                    print("error")
            else:
                valux = int(arg)
                p.start(valux)

                g = valt * valux/100
                print(f'{g:.2f}')

except KeyboardInterrupt:
     print("key ")       
        
    
finally:
    p.stop()
    GPIO.output(dac, 0)
    GPIO.cleanup()
