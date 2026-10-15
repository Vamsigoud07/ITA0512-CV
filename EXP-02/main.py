import cv2
img = cv2.imread('sample.jpg')
blur = cv2.GaussianBlur(img, (15, 15), 0)
cv2.imwrite('output.jpg', blur)
