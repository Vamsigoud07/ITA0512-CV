import cv2
img = cv2.imread('watch.jpg') # Dummy frame
# Draw simulated vehicle detections
cv2.rectangle(img, (10, 10), (100, 100), (0, 0, 255), 2)
cv2.imwrite('output.jpg', img)
