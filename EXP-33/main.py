import cv2
import numpy as np
img = np.ones((400, 400, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 0), 3)
cv2.imwrite('output.jpg', img)
