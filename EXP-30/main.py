import cv2
img = cv2.imread('sample.jpg')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)
for (x, y, w, h) in smiles:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
cv2.imwrite('output.jpg', img)
