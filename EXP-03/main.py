import cv2
img = cv2.imread('sample.jpg')
edges = cv2.Canny(img, 100, 200)
cv2.imwrite('output.jpg', edges)
