import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import espeak
import os

#Get obstacle
#setting parameter

GPIO.setmode(GPIO.BCM)
trig1 = 24
echo1 = 25

trig2 = 22
echo2 = 23

#trig3 = 24
#echo3 = 25

GPIO.setwarnings(False)

GPIO.setup(trig1,GPIO.OUT)
GPIO.setup(echo1,GPIO.IN)

GPIO.setup(trig2,GPIO.OUT)
GPIO.setup(echo2,GPIO.IN)

#GPIO.setup(trig3,GPIO.OUT)
#GPIO.setup(echo3,GPIO.IN)

GPIO.output(trig1,False)
GPIO.output(trig2,False)
#GPIO.output(trig3,False)


# initialize the camera
cam = cv2.VideoCapture(0)
ret, image = cam.read()

srcPath="/home/pi/Desktop"


print "Starting Camera"

if ret:
    cv2.imshow('SnapshotTest',image)
    cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    print "image Closed"
    cv2.imwrite('/home/pi/Desktop/SnapshotTest.jpg',image)
    cam.release()


def getString(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img,kernel,iterations = 1)

    cv2.imwrite(srcPath + "removed_noise.png", img)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11 ,2)
    cv2.imwrite(srcPath +"thres.png",img)
    result = pytesseract.image_to_string(Image.open(srcPath + "thres.png"))

    return result

print 'Start recognize text from image'

textfromString = getString(srcPath + "img1.png")
print(textfromString)
os.system('espeak '+textfromString)
while espeak.is_playing:
	pass                        





print "Measuring distance..."

print "waiting for sensor"
time.sleep(2)

GPIO.output(trig1,True)
GPIO.output(trig2,True)
#GPIO.output(trig3,True)
time.sleep(0.0001)
GPIO.output(trig1,False)
GPIO.output(trig2,False)
#GPIO.output(trig3,False)

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
