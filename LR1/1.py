import cv2

load_flags = cv2.IMREAD_COLOR
# IMREAD_COLOR, IMREAD_GRAYSCALE, IMREAD_UNCHANGED

show_flags = cv2.WINDOW_AUTOSIZE
# WINDOW_AUTOSIZE, WINDOW_NORMAL, WINDOW_KEEPRATIO

jpg_img = cv2.imread(r"images\katze.jpg", load_flags)
png_img = cv2.imread(r"images\katze.png", load_flags)
webp_img = cv2.imread(r"images\katze.webp", load_flags)

img_to_show = webp_img

cv2.namedWindow("Katze Window", show_flags)
cv2.imshow("Katze Window", img_to_show)
cv2.waitKey(0)

cv2.destroyAllWindows()