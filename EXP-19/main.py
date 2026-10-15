import cv2
import numpy as np
img = cv2.imread('sample.jpg')
kernel = np.ones((5,5), np.uint8)
erosion = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
cv2.imwrite('output.jpg', erosion)
