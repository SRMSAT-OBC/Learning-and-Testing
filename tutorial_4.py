import imp
import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

# Converting pixel to a specific color (BGR)
img[55, 55] = [255, 255, 255]
px = img[55, 55]
print(px)

# Region of Image
# ROI = img[100:150, 100:150]
# print(ROI)

# Converting a region to a specific color
# img[100:150, 100:150] = [255, 255, 255]

# Copying and pasting ROI
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
