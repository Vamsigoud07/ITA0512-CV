import cv2
img = cv2.imread('sample.jpg')
h, w, _ = img.shape
cv2.putText(img, 'WATERMARK', (w-200, h-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
cv2.imwrite('output.jpg', img)
