import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)

#using cv2

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#using matplotlib

plt.imshow(img,cmap='gray',interpolation='bicuble')
plt.show()