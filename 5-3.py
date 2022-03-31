import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4

troyka = 17

Bits = 8

Levels = 2**Bits

MaxVoltage = 3.3

signal = 0

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = 1) #, initial

GPIO.setup(comp, GPIO.IN)

def decimal2binary (value):
    return [int(num) for num in bin(value)[2:].zfill(8)]

def voltage (der):
    
    value = 0
    
    for i in range (8):
        value += der[i] / (2 ** (i + 1))     

    return value


def adc ():
    less = [0, 0, 0, 0, 0, 0, 0, 0]
    for counter in range (Bits):
        less[counter] = 1
        GPIO.output(dac, less)
        time.sleep(0.001)
        comparatorValue = GPIO.input(comp)
        if comparatorValue == 0:
            less[counter] = 0
        else:
            less[counter] = 1
    out = less[0] * 128 + less[1] * 64 + less[2] * 32 + less[3] * 16 + less[4]*8 + less[5] * 4 + less[6] * 2 + less[7]
    return out

try:
    while True:
        voltage = adc ()
        print("voltage is {:.2f} decimal is {}".format(voltage * MaxVoltage/Levels, voltage))
        time.sleep(0.1)
        

finally:
    GPIO.output (dac, 0)

    GPIO.output (troyka, 0)

    GPIO.cleanup (dac)
    GPIO.cleanup (troyka)