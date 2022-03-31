import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]

leds = [21, 20, 16, 12, 7, 8, 25, 24]

comp = 4

troyka = 17

Bits = 8

Levels = 2**Bits

MaxVoltage = 3.3

signal = 0

GPIO.setup(dac, GPIO.OUT)

GPIO.setup(leds, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial = 1) #, initial

GPIO.setup(comp, GPIO.IN)


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]




def adc():
    for counter in range (Levels):
        signal = decimal2binary(counter)
        GPIO.output(dac, signal)
        time.sleep(0.0005)
        comparatorValue = GPIO.input(comp)
        if comparatorValue == 0:
            print("ADC value = {}, {}".format(counter, signal))
            return counter


try:
    while True:
        voltage = adc() 
        print("voltage is {:.2f}".format(voltage/ Levels * MaxVoltage))

        number = round(Bits/Levels*voltage)
        print(number)

        GPIO.output(leds, decimal2binary(2**number-1))
        time.sleep(0.1)

except KeyboardInterrupt:
     print("key ")       
        
    
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()