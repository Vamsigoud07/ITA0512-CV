import cv2
img = cv2.imread('sample.jpg', 0)
_, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('output.jpg', thresh)
