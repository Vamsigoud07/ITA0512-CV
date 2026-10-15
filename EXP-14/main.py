import cv2
import numpy as np
img = cv2.imread('sample.jpg')
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (300,300))
cv2.imwrite('output.jpg', dst)
