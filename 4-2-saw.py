import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]

val = 0

GPIO.setup(dac, GPIO.OUT)


def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

try:
    valux = float(input("enter your period"))
    
    while True:
        for a in range(255):
            lit = a
            if lit < 256:
                if (int(lit) < 0 or int(lit) > 255):
                    print("error")
                else:
                    b = decimal2binary(int(lit))
                    print(b)
                    GPIO.output(dac, b)

                    

                    val  = 0
                    for a in range(8):
                        val += b[a]/(2)**(a+1)
                    g = 3.3 * val

                    print(f'{g:.2f}')
                    time.sleep(valux)
        
        for a in range(255):
            lit = 255 - a
            b = decimal2binary(int(lit))
            print(b)
            GPIO.output(dac, b)
            

            val  = 0
            for a in range(8):
                val += b[a]/(2)**(a+1)
            g = 3.3 * val

            print(f'{g:.2f}')
            time.sleep(valux)


except KeyboardInterrupt:
     print("key ")       
        
    
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()