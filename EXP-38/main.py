import cv2
img = cv2.imread('sample.jpg')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
print(f'Detected faces: {len(faces)}')
cv2.imwrite('output.jpg', img)
