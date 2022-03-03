import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]

aux = [22, 23, 27, 18, 15, 14, 3, 2]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

GPIO.output(leds, 1)
try:
    for a in range(0, 10):
        for led in range(0, 8):
            GPIO.output(leds[led], GPIO.input(aux[led]))
            time.sleep(0.2)
finally:        

    GPIO.output(leds, 0)


    GPIO.cleanup()