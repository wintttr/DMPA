import cv2
import numpy as np
lower_red = np.array([150, 150, 0])
upper_red = np.array([180, 255, 255])

def nothing(val):
    pass
    
def tracking():
    cap = cv2.VideoCapture(0)    
    cv2.namedWindow('Display1')
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
        
    while True:        
        ret, frame = cap.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        res = cv2.bitwise_and(frame, frame, mask=mask)
        
        cv2.erode(mask, kernel, iterations=1)
        cv2.dilate(mask,  kernel, iterations=1)
        
        frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        frame_threshold = cv2.inRange(frame_HSV, (0, 180, 80), (10, 255, 255))
        frame_threshold2 = cv2.inRange(frame_HSV, (170, 180, 80), (180, 255, 255))
        combine = frame_threshold + frame_threshold2
        
        opening = cv2.morphologyEx(combine, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)


        moments = cv2.moments(closing, 1)
        dm00 = moments['m00']
        dm10 = moments['m10']
        dm01 = moments['m01']
        
        if dm00 > 2500:
            x = dm10 // dm00
            y = dm01 // dm00
            cv2.rectangle(frame, (x - 100, y + 100), (x + 100, y - 100), (0,0,0), 3)
        
        cv2.imshow('Display1', frame)
        cv2.imshow('Display2', closing)
        
        if not ret:
            break        
        if cv2.waitKey(1) & 0xFF == 27:
            break
            
    cv2.destroyAllWindows()    
    cap.release()

if __name__ == '__main__':    
    tracking()