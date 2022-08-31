import cv2
import numpy as np
import matplotlib.pyplot as plt

# To import the image file in the code
img = cv2.imread("./watch.jpg", cv2.IMREAD_GRAYSCALE)

"""To Show image using cv2
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""To show image using matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
plt.show()
"""

"""To save the image using cv2
cv2.imwrite("./watchgray.jpg", img)
"""
