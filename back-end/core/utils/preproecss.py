import cv2
import numpy as np
import os


def proprocess(path):
    img = cv2.imread(path)
    img = cv2.resize(img, (512, 512))
    # 中值滤波
    # img = cv2.medianBlur(img, 3)

    imgr = img[:, :, 2]
    imgg = img[:, :, 1]
    imgb = img[:, :, 0]

    claher = cv2.createCLAHE(clipLimit=3, tileGridSize=(10, 18))
    claheg = cv2.createCLAHE(clipLimit=2, tileGridSize=(10, 18))
    claheb = cv2.createCLAHE(clipLimit=1, tileGridSize=(10, 18))
    cllr = claher.apply(imgr)
    cllg = claheg.apply(imgg)
    cllb = claheb.apply(imgb)

    img = np.dstack((cllb, cllg, cllr))
    img_name = path.split('/')[-1]
    cv2.imwrite("/Users/rune/PycharmProjects/Flask-VUE/back-end/processed/" + img_name, img)
    return "/Users/rune/PycharmProjects/Flask-VUE/back-end/processed/" + img_name


if __name__ == '__main__':
    proprocess("/Users/rune/PycharmProjects/Flask-VUE/back-end/uploads/0001.png")
