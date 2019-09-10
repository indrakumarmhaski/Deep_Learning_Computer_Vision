import keras
import matplotlib
import numpy as np 
import cv2

def sketchImage(image):
	img_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
	canny_edges = cv2.Canny(img_gray_blur,10,70)
	ret,mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY_INV)
	return mask

cap = cv2.VideoCapture(0)

while True:
	ret,frame = cap.read()
	cv2.imshow('Live Sketch',sketchImage(frame))
	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()