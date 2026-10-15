import cv2
img = cv2.imread('sample.jpg')
cv2.putText(img, 'OpenCV Task', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
cv2.imwrite('output.jpg', img)
