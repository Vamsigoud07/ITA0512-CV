import cv2
img = cv2.imread('sample.jpg', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
cv2.imwrite('output.jpg', sobelx)
