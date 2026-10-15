import cv2
import numpy as np
h, w = 400, 400
img = np.ones((h, w, 3), dtype=np.uint8) * 255
b_size = h // 10
img[0:b_size, 0:b_size] = [0, 0, 0] # Black
img[0:b_size, w-b_size:w] = [255, 0, 0] # Blue
img[h-b_size:h, 0:b_size] = [0, 255, 0] # Green
img[h-b_size:h, w-b_size:w] = [0, 0, 255] # Red
cv2.imwrite('output.jpg', img)
