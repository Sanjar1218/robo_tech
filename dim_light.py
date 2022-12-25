# type: ignore
import RPi.GPIO as gp
import time

led = 7
switch1= 37
switch2 = 35
cycle = 50

gp.setmode(gp.BOARD)
gp.setup(led, gp.OUT)

gp.setup(switch1, gp.IN, pull_up_down=gp.PUD_UP)
gp.setup(switch2, gp.IN, pull_up_down=gp.PUD_UP)
pwm = gp.PWM(led, 60)
pwm.start(cycle)
p_switch1 = 1
p_switch2 = 1
rang = 10

try:
	while True:
		input1 = gp.input(switch1)
		input2 = gp.input(switch2)
		
		if input1 == 0:
			p_switch1 = 0
		if input2 == 0:
			p_switch2 = 0
			
		if p_switch1 == 0 and input1 == 1:
			p_switch1 = 1
			if cycle < 100:
				cycle += rang
				pwm.ChangeDutyCycle(cycle)
		if p_switch2 == 0 and input2 == 1:
			p_switch2 = 1
			if cycle > 0:
				cycle -= rang
				pwm.ChangeDutyCycle(cycle)
		time.sleep(0.1)
except KeyboardInterrupt:
	gp.cleanup()
