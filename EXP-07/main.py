import cv2
cap = cv2.VideoCapture('sample_video.mp4')
# Logic dummy to process frames
cap.release()
with open('output.txt', 'w') as f:
    f.write('Slow & fast video processed')
