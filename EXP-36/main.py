import cv2
import numpy as np
img = cv2.imread('sample.jpg')
# Basic threshold background removal
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite('output.jpg', res)
