import cv2
import numpy as np
img = cv2.imread('sample.jpg')
hist_b = cv2.calcHist([img], [0], None, [256], [0, 256])
# Create dummy image to save representing success
cv2.imwrite('output.jpg', img)
