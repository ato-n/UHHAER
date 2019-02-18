import RPi.GPIO as GPIO
import random

GPIO.setmode(GPIO.BCM)
	
def setupGPIO():
	GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(9, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(10, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW)

	GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def allonGPIO():
	GPIO.output(5, GPIO.HIGH)
	GPIO.output(6, GPIO.HIGH)
	GPIO.output(7, GPIO.HIGH)
	GPIO.output(8, GPIO.HIGH)
	GPIO.output(9, GPIO.HIGH)
	GPIO.output(10, GPIO.HIGH)
	GPIO.output(11, GPIO.HIGH)
	GPIO.output(12, GPIO.HIGH)
	GPIO.output(13, GPIO.HIGH)
	GPIO.output(16, GPIO.HIGH)
	GPIO.output(19, GPIO.HIGH)
	GPIO.output(20, GPIO.HIGH)
	GPIO.output(21, GPIO.HIGH)
	GPIO.output(22, GPIO.HIGH)
	GPIO.output(23, GPIO.HIGH)
	GPIO.output(24, GPIO.HIGH)
	GPIO.output(25, GPIO.HIGH)
	GPIO.output(26, GPIO.HIGH)

def alloffGPIO():
	GPIO.output(5, GPIO.LOW)
	GPIO.output(6, GPIO.LOW)
	GPIO.output(7, GPIO.LOW)
	GPIO.output(8, GPIO.LOW)
	GPIO.output(9, GPIO.LOW)
	GPIO.output(10, GPIO.LOW)
	GPIO.output(11, GPIO.LOW)
	GPIO.output(12, GPIO.LOW)
	GPIO.output(13, GPIO.LOW)
	GPIO.output(16, GPIO.LOW)
	GPIO.output(19, GPIO.LOW)
	GPIO.output(20, GPIO.LOW)
	GPIO.output(21, GPIO.LOW)
	GPIO.output(22, GPIO.LOW)
	GPIO.output(23, GPIO.LOW)
	GPIO.output(24, GPIO.LOW)
	GPIO.output(25, GPIO.LOW)
	GPIO.output(26, GPIO.LOW)

def on_record(daysecs):
	if daysecs >= 27600 and daysecs <= 54300:
		if daysecs >= 30300 and daysecs <= 30600 or daysecs >= 33300 and daysecs <= 34200 or daysecs >= 39600 and daysecs <= 40800 or daysecs >= 43500 and daysecs <= 43800 or daysecs >= 46500 and daysecs <= 48600 or daysecs >= 51300 and daysecs <= 54300:
			return False
		else:
			return True
	else:
		return False

def aprilfool():
	randomint = random.randint(0, 17)
	if randomint == 0:
		alloffGPIO()
		GPIO.output(5, GPIO.HIGH)
	elif randomint == 1:
		alloffGPIO()
		GPIO.output(6, GPIO.HIGH)
	elif randomint == 2:
		alloffGPIO()
		GPIO.output(7, GPIO.HIGH)
	elif randomint == 3:
		alloffGPIO()
		GPIO.output(8, GPIO.HIGH)
	elif randomint == 4:
		alloffGPIO()
		GPIO.output(9, GPIO.HIGH)
	elif randomint == 5:
		alloffGPIO()
		GPIO.output(10, GPIO.HIGH)
	elif randomint == 6:
		alloffGPIO()
		GPIO.output(11, GPIO.HIGH)
	elif randomint == 7:
		alloffGPIO()
		GPIO.output(12, GPIO.HIGH)
	elif randomint == 8:
		alloffGPIO()
		GPIO.output(13, GPIO.HIGH)
	elif randomint == 9:
		alloffGPIO()
		GPIO.output(16, GPIO.HIGH)
	elif randomint == 10:
		alloffGPIO()
		GPIO.output(19, GPIO.HIGH)
	elif randomint == 11:
		alloffGPIO()
		GPIO.output(20, GPIO.HIGH)
	elif randomint == 12:
		alloffGPIO()
		GPIO.output(21, GPIO.HIGH)
	elif randomint == 13:
		alloffGPIO()
		GPIO.output(22, GPIO.HIGH)
	elif randomint == 14:
		alloffGPIO()
		GPIO.output(23, GPIO.HIGH)
	elif randomint == 15:
		alloffGPIO()
		GPIO.output(24, GPIO.HIGH)
	elif randomint == 16:
		alloffGPIO()
		GPIO.output(25, GPIO.HIGH)
	elif randomint == 17:
		alloffGPIO()
		GPIO.output(26, GPIO.HIGH)