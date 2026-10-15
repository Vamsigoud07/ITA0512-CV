import cv2
img = cv2.imread('sample.jpg', 0)
equalized = cv2.equalizeHist(img)
cv2.imwrite('output.jpg', equalized)
