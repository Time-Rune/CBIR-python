import cv2
import numpy as np
from skimage import feature, exposure


def get_shape_fea(path):
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = np.float32(image) / 255.0  # 归一化

    fd = feature.hog(image, orientations=9, pixels_per_cell=(32, 32),
                     cells_per_block=(2, 2))

    return fd
