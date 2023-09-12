import cv2

cap = cv2.VideoCapture("rtsp://10.182.214.63:1024/h264_pcm.sdp")
cap.set(3, 640)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break