import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-10 104828.png", cv2.IMREAD_GRAYSCALE)

# Apply the Sobel operator
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine the horizontal and vertical edges
edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Display the result
cv2.imshow('Image', img)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
