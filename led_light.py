# type: ignore
import RPi.GPIO as GPIO
import time

switch = 31

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.IN)

for i in range(10):
    print('Switch status = ', GPIO.input(switch))
    time.sleep(0.1)

GPIO.cleanup()