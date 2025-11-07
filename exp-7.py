import cv2 
import numpy as np 
# Load the image 
image_path  =  "..\\lena.png"  
#  Replace with the path to your  image  
img = cv2.imread(image_path) 
# Get the height and width of the image 
height, width, _ = img.shape 
up_left = img[0:height//2, 0:width//2] 
up_right = img[0:height//2, width//2:width] 
down_left = img[height//2:height, 0:width//2] 
down_right = img[height//2:height, width//2:width] 
# Create a blank canvas to display the quadrants 
canvas = np.zeros((height+3, width+3, 3), dtype=np.uint8) 
# Place the quadrants on the canvas 
canvas[1:height//2+1, 1:width//2+1]  =  up_left  
canvas[1:height//2+1, width//2+3:width+3]  =  up_right  
canvas[height//2+3:height+3, 1:width//2+1] = down_left 
canvas[height//2+3:height+3, width//2+3:width+3] = down_right 
#  Display the canvas  
cv2.imshow("Image Quadrants", canvas)   
cv2.waitKey(0)