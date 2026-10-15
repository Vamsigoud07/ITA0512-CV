import cv2
import numpy as np
img = cv2.imread('sample.jpg')
kernel = np.ones((5,5), np.uint8)
eroded = cv2.erode(img, kernel, iterations=1)
cv2.imwrite('output.jpg', eroded)
