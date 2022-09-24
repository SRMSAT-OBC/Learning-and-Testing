import cv2
import numpy as np
import matplotlib.pyplot as plt

#                              0
img=cv2.imread('Flower 1.jpg',1)
#IMREAD_COLOR - 1
#IMREAD_UNCHANGED = -1

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([1009,1060],[101,408],'y',linewidth=5)
plt.show()
