import cv2
import numpy as np
import os


def pre_process_one(path):
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
    return img


def pre_process():
    path = '/Users/rune/PycharmProjects/Flask-VUE/back-end/dataset/image_data'
    for p in os.listdir(path):
        img = cv2.imread(os.path.join(path, p))
        cv2.imshow("img0", img)

        img = cv2.resize(img, (512, 512))
        # 中值滤波
        # img = cv2.medianBlur(img, 3)

        cv2.imshow("img", img)

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

        cv2.imshow("zq", img)
        cv2.waitKey()

        # cv2.imwrite("/Users/rune/PycharmProjects/Flask-VUE/back-end/dataset/image_processed/" + p, img)


if __name__ == '__main__':
    pre_process()
