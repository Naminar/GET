import RPi.GPIO as gpio
from time import sleep 
from time import time
from threading import Thread
import matplotlib.pyplot as plt

gpio.setmode(gpio.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

gpio.setup(leds, gpio.OUT)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = 0)
gpio.setup(comp, gpio.IN)

""" some fundtion to binary transformation:"""

""" transrormation to list val number """

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

""" transrormation val number to list  """

def bin_to_dec(bits):
    dec = 0
    code = 1
    for i in range(7, -1, -1):
        dec += bits[i] * codegpio.output(leds, )
        code *= 2
    return dec
""" ADC function with leds out"""
def adc():
    voltage = 8*[0]
    
    gpio.output(dac, 0)

    sleep(0.01)

    for st in range(0, 8):
        voltage[st] = 1

        gpio.output(dac[st], voltage[st])

        sleep(0.0001)

        if (gpio.input(comp) == 0): # led is on
            voltage[st] = 0
            gpio.output(dac[st], voltage[st])

    gpio.output(leds, voltage)

    dec = bin_to_dec(voltage)
    return dec
 
""" creat list and other variables for time and dec -- to adc function """

value = []
startT = 0
stopT  = 0
dec = 0

try:
    startT = time()
    gpio.output(troyka, 1)

    """ make to increase result value """
    
    while (dec < 0.99 * 3):
        
        print(dec)
        
        dec = adc() / 256.0 * 3.3
        
        print("Adc Volage+ = {:.3} v, volage code = {}".format(dec, dec * 256 / 3.3))

        value.append(dec)

    gpio.output(troyka, 0)

    """ make to dencrease result value"""


    while (dec > 0.01 * 3.3):

        dec = adc()/ 256.0 * 3.3
        print("Adc Volage- = {:.3} v, volage code = {}".format(dec, dec * 256 / 3.3))
        
        value.append(dec)

    stopT = time()

    """ write result value to file """

    with open('measureData.txt', 'w') as f:
        f.write('\n'.join([str(val) for val in value]))

    expTime = stopT - startT

    """ write intormation result to file """


    with open('settings.txt', 'w') as f:
        f.write('Время измерения, с {:.6f}'.format(expTime))
        f.write('Шаг квантования, В {:.6f}'.format(3.3 / 256))

    print(expTime)
    
    T = 0

    t = [val * T for val in range(0, len(value))]

    plt.plot(value)
    plt.show()

    print('Время измерения, с', expTime)
    print('Период измерения, с', expTime /  len(value))
    print('Частота дискр, Гц', len(value) / expTime)
    print('Шаг квантования, В', 3.3 / 256)
    
    """  the end """
    
finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()