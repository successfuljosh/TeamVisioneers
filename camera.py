import cv2
import numpy as np

# initialize the camera
cam = cv2.VideoCapture(0)
ret, image = cam.read()

srcPath="/home/pi/Desktop/"


print "HEllo"

if ret:
    cv2.imshow('SnapshotTest',image)
    cv2.waitKey(0)
    cv2.destroyWindow('SnapshotTest')
    cv2.imwrite('/home/pi/Desktop/SnapshotTest.jpg',image)
cam.release()


def getString(imgPath):
    img = cv2.imread(imgPath)
    img = cv2.cvtColor(img, cv2.COLO_BGR2GRAY)
    kernel = np.ones((1,1), np.uint8)
    img = cv2.dilate(img,kernel,iterations = 1)

    cv2.imwrite(srcPath + "removed_noise.png", img)
    img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11 ,2)
    cv2.imwrite(srcPath +"thres.png",img)
    result = pytesseract.image_to_string(Image.open(srcPath + "thres.png"))

    return result

print 'Start recognize text from image'

textfromString = getString(srcPath + "1.png")
print(textfromString)
                                
