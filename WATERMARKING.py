import cv2
import numpy as np

img1 = cv2.imread("C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-10 104828.png")
img2 = cv2.imread("C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-11 104828.png")

x, y, w, h = 100, 100, 200, 200
crop_img = img1[y:y+h, x:x+w]

x, y = 300, 200
img1[y:y+h, x:x+w] = img2

cv2.imshow('Cropped Image', crop_img)
cv2.imshow('Pasted Image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
