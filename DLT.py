import numpy as np
import cv2

# define the source and destination points
pts_src = np.array([[141, 131], [480, 159], [493, 630],[64, 601]])
pts_dst = np.array([[318, 256],[534, 372],[316, 670],[73, 473]])

# compute the homography matrix
h, status = cv2.findHomography(pts_src, pts_dst)

# read the source image and apply the transformation
img_src = cv2.imread("C:/Users/INDHU/Downloads/pG07kr.jpg")
img_dst = cv2.warpPerspective(img_src, h, (img_src.shape[1], img_src.shape[0]))

# display the images
cv2.imshow('Source Image', img_src)
cv2.imshow('Destination Image', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
