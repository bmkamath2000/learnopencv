import cv2 as cv
import numpy as np 

img = cv.imread('.\\lena.png')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

contour_image = img.copy() 
cv.drawContours(contour_image, contours, -1, (0, 255, 0), 3) 

cv.imshow('Original Image', img) 
cv.imshow('Contours', contour_image) 
cv.waitKey(0)