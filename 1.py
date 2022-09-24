import cv2
import numpy as np
import matplotlib.pyplot as plt
#                              0
img=cv2.imread('Flower 1.jpg',1)
#IMREAD_COLOR - 1
#IMREAD_UNCHANGED = -1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

