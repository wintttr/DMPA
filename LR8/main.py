import time

import cv2
from yoloface import face_analysis


class HaarClassifier:
    def __init__(self):
        self.detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def detect(self, frame):
        new_frame = frame.copy()
        faces = self.detector.detectMultiScale(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

        for (x, y, w, h) in faces:
            cv2.rectangle(new_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        return new_frame


class YoloClassifier:
    def __init__(self):
        self.face = face_analysis()

    def detect(self, frame):
        _, box, conf = self.face.face_detection(frame_arr=frame, frame_status=True, model='tiny')
        return self.face.show_output(frame, box, frame_status=True)


def process_video(cap, detector):
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Video finished")
            break

        cv2.imshow("", detector.detect(frame))

    cap.release()


def main():
    detector = YoloClassifier()
    process_video(cv2.VideoCapture(0), detector)

    # image = cv2.imread("faces.jpg")

    # begin = time.time()
    # new_image = detector.detect(image)
    # end = time.time()

    # cv2.imwrite("haar_faces.jpg", new_image)

    # print(f"Estimated time: {end - begin}")


main()
