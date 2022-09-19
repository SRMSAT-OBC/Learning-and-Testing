import cv2
import numpy as np

img1=cv2.imread('3D-Matplotlib.png')
img2=cv2.imread('mainlogo.png')

rows,cols,channels=img2.shape;
roi=img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img_fg= cv2.bitwise_and(ing2, img2, mask=mask)

dst = cv2.add(img1_bg,img_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst',dst)

cv2.WaitKey(0)
cv2.destroyAllWindows()

