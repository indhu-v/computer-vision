import numpy as np
import cv2

# Define the source and destination points
src_pts = np.array([[0, 0], [0, 100], [100, 100], [100, 0]], dtype=np.float32)
dst_pts = np.array([[50, 50], [10, 90], [90, 90], [50, 10]], dtype=np.float32)

# Compute the homography matrix
H, _ = cv2.findHomography(src_pts, dst_pts)

# Print the homography matrix
print('Homography Matrix:')
print(H)
