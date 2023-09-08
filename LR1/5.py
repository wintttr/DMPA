import cv2

img = cv2.imread(r"images\katze.png", cv2.IMREAD_UNCHANGED)

cv2.imshow("original", img)
cv2.imshow("hsv", cv2.cvtColor(img, cv2.COLOR_BGR2HSV))

cv2.waitKey(0)
cv2.destroyAllWindows()
