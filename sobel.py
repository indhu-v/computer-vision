import cv2
import numpy as np

# Load the image in grayscale
img = cv2.imread("C:/Users/INDHU/Downloads/pG07kr.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Sobel detection
dx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
dy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
mag = np.sqrt(dx**2 + dy**2)

# Normalize and convert to uint8
mag = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Detection', mag)
cv2.waitKey(0)
cv2.destroyAllWindows()
