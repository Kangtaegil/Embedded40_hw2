import RPi.GPIO as GPIO
import time

TRIG = 5
ECHO = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)

time.sleep(.3)

motor = GPIO.PWM(20,50)

motor.start(7.5)

while True:
	motor.ChangeDutyCycle(7.5)
	time.sleep(.4)
	motor.ChangeDutyCycle(12.5)
	time.sleep(.4)
	motor.ChangeDutyCycle(2.5)
	time.sleep(.4)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	print "Distance: ", distance, "cm"

	inputValue = GPIO.input(24)

	if(inputValue == True or distance < 5):
		break;

GPIO.cleanup()

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

try:
	while True:
		GPIO.output(21, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(21, GPIO.LOW)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
