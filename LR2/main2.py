import cv2

window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'

# capture = cv2.VideoCapture(r"videoSample.mp4")
capture = cv2.VideoCapture(0)


kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
while True:
    ret, frame = capture.read()

    if not ret:
        break

    cv2.namedWindow(window_capture_name, cv2.WINDOW_NORMAL)
    cv2.namedWindow(window_detection_name, cv2.WINDOW_NORMAL)

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    frame_threshold = cv2.inRange(frame_HSV, (0, 150, 80), (25, 255, 255))
    frame_threshold2 = cv2.inRange(frame_HSV, (160, 150, 80), (180, 255, 255))
    
    combine = frame_threshold + frame_threshold2

    opening = cv2.morphologyEx(combine, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    
    moments = cv2.moments(closing, 1)
    dm00 = moments['m00']
    dm10 = moments['m10']
    dm01 = moments['m01']

    if dm00 > 2500:
        # x = int(dm10 // dm00)
        # y = int(dm01 // dm00)
        # cv2.rectangle(frame, (x - 100, y - 100), (x + 100, y + 100), (0,0,0), 3)
        x, y, w, h = cv2.boundingRect(closing)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,0,0), 3)


    cv2.imshow(window_capture_name, frame)
    cv2.imshow(window_detection_name, closing)

    if cv2.waitKey(1) & 0xFF == 27:
        break