import cv2


def draw_plus(img, color, thickness=2, blurness=True):
    h = img.shape[0]
    w = img.shape[1]

    h_ul = tuple(map(int, (w * 0.2, h * 0.45)))
    h_dr = tuple(map(int, (w * (1 - 0.2), h * (1 - 0.45))))

    v_ul = tuple(map(int, (w * 0.45, h * 0.1)))
    v_dr = tuple(map(int, (w * (1 - 0.45), h * (1 - 0.1))))

    cv2.rectangle(img, v_ul, v_dr, color, thickness)

    if blurness:
        blurred = img[h_ul[1]:h_dr[1], h_ul[0]:h_dr[0]]
        blurred = cv2.blur(blurred, (15, 15))
        img[h_ul[1]:h_dr[1], h_ul[0]:h_dr[0]] = blurred

    cv2.rectangle(img, h_ul, h_dr, color, thickness)
