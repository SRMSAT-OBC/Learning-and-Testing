import imp
import numpy as np
import cv2

img = cv2.imread('watch', cv2.IMREAD_COLOR)

# pixel to a specific color

img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)


watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
