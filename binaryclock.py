import time
import RPi.GPIO as GPIO
import binclockfunctions as binclock

#GPIOs hour: 5 6 7 8 9
#GPIOs on_record: 10
#GPIOs minute: 11 12 13 16 19 20
#GPIOs second: 21 22 23 24 25 26

GPIO.setmode(GPIO.BCM)

binclock.setupGPIO()
binclock.allonGPIO()
binclock.alloffGPIO()

aprilfool = False #<- Set to True to activate the aprilfoolfunction

while True:	
	clocktime = time.localtime()
	hour = str("{0:05b}".format(clocktime[3]))
	minute = str("{0:06b}".format(clocktime[4]))
	second = str("{0:06b}".format(clocktime[5]))
	daysecs = int(clocktime[3]*60*60+clocktime[4]*60+clocktime[5])
		on_record = binclock.on_record(daysecs)
		if clocktime[1] == 4 and clocktime[2] == 1 and aprilfool == True:
		binclock.aprilfool()
	
	if int(hour[-1]):
		GPIO.output(5, GPIO.HIGH)
	else:
		GPIO.output(5, GPIO.LOW)
	if int(hour[-2]):
		GPIO.output(6, GPIO.HIGH)
	else:
		GPIO.output(6, GPIO.LOW)
	if int(hour[-3]):
		GPIO.output(7, GPIO.HIGH)
	else:
		GPIO.output(7, GPIO.LOW)
	if int(hour[-4]):
		GPIO.output(8, GPIO.HIGH)
	else:
		GPIO.output(8, GPIO.LOW)
	if int(hour[-5]):
		GPIO.output(9, GPIO.HIGH)
	else:
		GPIO.output(9, GPIO.LOW)
	if int(on_record):
		GPIO.output(10, GPIO.HIGH)
	else:
		GPIO.output(10, GPIO.LOW)
	if int(minute[-1]):
		GPIO.output(11, GPIO.HIGH)
	else:
		GPIO.output(11, GPIO.LOW)
	if int(minute[-2]):
		GPIO.output(12, GPIO.HIGH)
	else:
		GPIO.output(12, GPIO.LOW)
	if int(minute[-3]):
		GPIO.output(13, GPIO.HIGH)
	else:
		GPIO.output(13, GPIO.LOW)
	if int(minute[-4]):
		GPIO.output(16, GPIO.HIGH)
	else:
		GPIO.output(16, GPIO.LOW)
	if int(minute[-5]):
		GPIO.output(19, GPIO.HIGH)
	else:
		GPIO.output(19, GPIO.LOW)
	if int(minute[-6]):
		GPIO.output(20, GPIO.HIGH)
	else:
		GPIO.output(20, GPIO.LOW)
	if int(second[-1]):
		GPIO.output(21, GPIO.HIGH)
	else:
		GPIO.output(21, GPIO.LOW)
	if int(second[-2]):
		GPIO.output(22, GPIO.HIGH)
	else:
		GPIO.output(22, GPIO.LOW)
	if int(second[-3]):
		GPIO.output(23, GPIO.HIGH)
	else:
		GPIO.output(23, GPIO.LOW)
	if int(second[-4]):
		GPIO.output(24, GPIO.HIGH)
	else:
		GPIO.output(24, GPIO.LOW)
	if int(second[-5]):
		GPIO.output(25, GPIO.HIGH)
	else:
		GPIO.output(25, GPIO.LOW)
	if int(second[-6]):
		GPIO.output(26, GPIO.HIGH)
	else:
		GPIO.output(26, GPIO.LOW)
else:
	binclock.alloffGPIO()
