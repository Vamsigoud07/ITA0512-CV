import cv2
img = cv2.imread('sample.jpg')
big_img = cv2.resize(img, (0,0), fx=2, fy=2)
small_img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
cv2.imwrite('output.jpg', big_img)
