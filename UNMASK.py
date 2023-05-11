import cv2
import numpy as np

img = cv2.imread("C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-10 100127.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)
sharpened = cv2.addWeighted(gray, 1.5, blurred, -0.5, 0)

cv2.imshow('Original', gray)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
