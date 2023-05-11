import cv2
import numpy as np

img = cv2.imread("C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-10 104828.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
gradient = cv2.magnitude(sobelx, sobely)

k = 0.5
sharpened = gray + k*gradient

cv2.imshow('Original', gray)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
