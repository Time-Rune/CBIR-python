import numpy as np
from skimage.color import rgb2hsv
import cv2


# 定义一个求三阶颜色矩的函数
def var(x):
    mid = np.mean(((x - x.mean()) ** 3))
    return np.sign(mid) * abs(mid) ** (1 / 3)


def color_moment(path):
    img = cv2.imread(path)

    img_hsv = rgb2hsv(img)
    img_h, img_s, img_v = img_hsv[:, :, 0], img_hsv[:, :, 1], img_hsv[:, :, 2]

    # 提取一阶矩，均值
    h_mean = np.mean(img_h)
    s_mean = np.mean(img_s)
    v_mean = np.mean(img_v)

    # 提取二阶矩，方差
    h_var = np.std(img_h)
    s_var = np.std(img_s)
    v_var = np.std(img_v)

    # 提取三阶矩
    h_third = var(img_h)
    s_third = var(img_s)
    v_third = var(img_v)

    color_moment = np.array([h_mean, s_mean, v_mean, h_var, s_var, v_var, h_third, s_third, v_third], dtype=np.float32)

    return color_moment
