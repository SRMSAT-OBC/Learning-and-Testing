import numpy as np
import cv2

img = cv2.imread('plant1.jpeg', cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(255,0,0),15)
cv2.rectangle(img, (150,300),(300,600),(0,155,0),19)
cv2.circle(img,(300,63),99,(0,0,199),-1)
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], False, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Haaruyi Here!',(10,500), font, 6, (200,255,155), 13, cv2.LINE_AA)

cv2.imshow('+image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
