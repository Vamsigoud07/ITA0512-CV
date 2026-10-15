import cv2
img = cv2.imread('sample.jpg')
roi = img[100:300, 100:300]
img[0:200, 0:200] = roi
cv2.imwrite('output.jpg', img)
