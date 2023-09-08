import cv2
from drawplus import draw_plus

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    draw_plus(frame, (0, 0, 255))

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break