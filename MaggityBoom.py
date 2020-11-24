import numpy as np
import pyautogui
import imutils
import pytesseract
import cv2

def screenshot():
	image = pyautogui.screenshot(region=(0,525, 100, 12)) #pyautogui.screenshot()
	image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
	cv2.imwrite("in_memory_to_disk.png", image)

screenshot()
conf = r'--oem 3 --psm 6 outputbase digits'
pytesseract.pytesseract.tesseract_cmd = "E:\\#FreakingMagicalThingThatCanDestroryEverythingIfInstalledIncorrectly\\tesseract.exe"
#print(pytesseract.pytesseract.tesseract_cmd)
img = cv2.imread('E:\\in_memory_to_disk.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
a=print(pytesseract.image_to_string(img,config=conf))

### I tried to convert the string I get from image_to_string method to int.
### That didn't work. Idk why. Seems like image_to_string
### returns you something different from a string.
#b=int(a)
#c=hex(b)
#print(b)
#print(c)

### This part of code is responsible for drawing squares and letters near
### identified symbols. Useless in my case so I commented it out.
#hImg,wImg,_ = img.shape
#boxes = pytesseract.image_to_data(img,config=conf)
#for x,b in enumerate(boxes.splitlines()):
#	if x!=0:
#		b = b.split()
#		print(b)
#		if len(b) == 12:
#			x,y,w,h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
#			cv2.rectangle(img, (x,y), (w+x,h+y),(0,0,255),3)
#			cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(25,25,255),1)

### Diplays the picture and waits till you press something. 
cv2.imshow('Result', img)
cv2.waitKey(0)