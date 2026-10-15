import cv2
img = cv2.imread('watch.jpg')
# Simulating basic visual bounding box around watch
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 2)
cv2.imwrite('output.jpg', img)
