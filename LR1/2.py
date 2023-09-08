import cv2

window_flags = cv2.WINDOW_AUTOSIZE
cv2.namedWindow('frame', window_flags)

cap = cv2.VideoCapture(r"video\katze.mp4", cv2.CAP_ANY)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(12) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
