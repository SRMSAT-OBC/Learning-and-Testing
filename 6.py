import cv2
import numpy as np

img = cv2.imread('plant1.jpeg',cv2.IMREAD_COLOR)

px = img[55,55]
img[55,55] = [255,255,255]

px = img[55,55]
print(px)

px = img[500:750,500:750]
print(px)

img[500:750,500:750] = [255,255,255]

print(img.shape)
print(img.size)
print(img.dtype)

plant = img[350:450,150:250]
img[0:100,0:100] = plant

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
