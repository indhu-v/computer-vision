import cv2
import numpy as np

img=cv2.imread("C:/Users/INDHU/Downloads/pG07kr.jpg")
re=cv2.resize(img,(250,250))
cv2.imshow("resize",re)
cv2.waitKey(0)
cv2.destroyAllWindows()
