import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

trig1 = 20
echo2 = 21

trig2 = 22
echo2 = 23

trig3 = 24
echo3 = 25

print "Measuring distance..."

GPIO.setup(trig1,GPIO.OUT)
GPIO.setup(echo1,GPIO.IN)

GPIO.setup(trig2,GPIO.OUT)
GPIO.setup(echo2,GPIO.IN)

GPIO.setup(trig3,GPIO.OUT)
GPIO.setup(echo3,GPIO.IN)

GPIO.output(trig1,False)
GPIO.output(trig2,False)
GPIO.output(trig3,False)

print "waiting for sensor"
time.sleep(2)

GPIO.output(trig1,True)
GPIO.output(trig2,True)
GPIO.output(trig3,True)
time.sleep(0.0001)
GPIO.output(trig1,False)
GPIO.output(trig2,False)
GPIO.output(trig3,False)

#sensor 1
while GPIO.input(echo1) == 0:
    pulse_start1 = time.time()
while GPIO.input(echo1) ==1:
    pulse_end1 = time.time()
pulse_duration1 = pulse_end1 - pulse_start1
distance1 = round(pulse_duration1 * 17150,2)

while distance1 < 50:
    os.system('espeak "Obstacle Detected!"')
while espeak.is_playing:
	pass

#sensor 2
while GPIO.input(echo2) == 0:
    pulse_start2 = time.time()
while GPIO.input(echo2) ==1:
    pulse_end2 = time.time()
pulse_duration2 = pulse_end2 - pulse_start2
distance2 = round(pulse_duration2 * 17150, 2)

#sensor 3
while GPIO.input(echo3) == 0:
    pulse_start3 = time.time()
while GPIO.input(echo3) ==1:
    pulse_end3 = time.time()
pulse_duration3 = pulse_end3 - pulse_start3
distance3 = round(pulse_duration3 * 17150, 2)

