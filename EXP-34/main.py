import cv2
import numpy as np
img = np.ones((400, 400, 3), dtype=np.uint8) * 255
cv2.circle(img, (200, 200), 100, (0, 0, 0), 3)
cv2.imwrite('output.jpg', img)
