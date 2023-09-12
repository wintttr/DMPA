import cv2

video = cv2.VideoCapture(0)

w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter.fourcc(*'XVID')
video_writer = cv2.VideoWriter('output.mov', fourcc, 25, (w, h))
while True:
    ok, img = video.read()
    cv2.imshow('img', img)
    video_writer.write(img)
    if cv2.waitKey(10) & 0xFF == 27:
        video_writer.release()
        break
video.release()
cv2.destroyAllWindows()