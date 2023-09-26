import cv2
import numpy as np
import sys
import os

import blur


class ArgumentError(Exception):
    pass


def get_filename():
    path = sys.argv[1]
    if os.path.isfile(path):
        return path
    else:
        raise ArgumentError(f"Файла {path} не существует")


def get_dim():
    d = sys.argv[2]
    if d.isdecimal() and int(d) % 2 == 1:
        return int(d)
    else:
        raise ArgumentError(f"Размерность матрицы - нечётное число")


def get_sigm():
    s = sys.argv[3]
    if s.isnumeric():
        return float(s)
    else:
        raise ArgumentError(f"Сигма - вещественное число")


def main():
    if len(sys.argv) != 4:
        print(f"Usage: {os.path.basename(sys.argv[0])} image dim sigm")
        print("\timage - path to image")
        print("\tdim - dimension of gaussian kernel")
        print("\tsigm - nu eto ponyatno chto")
        exit(1)

    try:
        img = cv2.imread(get_filename())
        d = get_dim()
        sigm = get_sigm()

        channels = cv2.split(img)

        channels = tuple(map(lambda x: blur.blur(x, d, sigm), channels))

        blur_img = cv2.merge(channels)

        cv2.imshow("original", img)
        cv2.imshow("blurred", blur_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except ArgumentError as err:
        print("Ошибочка в аргументах:", err)

    except Exception as err:
        print("АААААААААААА ПРОИЗОШЛО ЧТО-ТО ПЛОХООООЕЕЕЕЕЕ")
        print("А именно:", err)


main()
