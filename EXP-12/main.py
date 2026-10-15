import cv2
img = cv2.imread('sample.jpg')
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('output.jpg', rotated)
