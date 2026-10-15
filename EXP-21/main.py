import cv2
import numpy as np
img = cv2.imread('sample.jpg')
kernel = np.ones((5,5), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite('output.jpg', opening)
