import cv2
import numpy as np
from drawplus import draw_plus

def maximized_color(clr):
    if clr[0] >= (clr[1] and clr[2]):
        return (255, 0, 0)
    elif clr[1] >= (clr[0] and clr[2]):
        return (0, 255, 0)
    elif clr[2] >= (clr[0] and clr[1]):
        return (0, 0, 255)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    h = frame.shape[0]
    w = frame.shape[1]

    color = frame[np.int16(w / 2), np.int16(h / 2)]

    draw_plus(frame, maximized_color(color), -1, False)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break