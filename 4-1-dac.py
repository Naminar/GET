import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]

val = 0

GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while True:
        lit = input("[0, 255] :")
        if lit.isdigit():
            if (int(lit) < 0 or int(lit) > 255):
                print("error")
            else:
                b = decimal2binary(int(lit))
                print(b)
                GPIO.output(dac, b)


                for a in range(8):
                    val += b[a]/(2)**(a)
                g = 3.3 * val

                print(f'{g:.2f}')
                #time.sleep(4)

        
        
        if(lit == 'q'):
            print("error x")

except KeyboardInterrupt:
     print("key ")       
        
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()