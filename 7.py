import cv2
import numpy as np

img1 = cv2.imread('anime5.jpg')
img2 = cv2.imread('anime6.png')

add_n = img1 + img2
add = cv2.add(img1,img2)

cv2.imshow('add_n',add_n)
cv2.imshow('add',add)

weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
