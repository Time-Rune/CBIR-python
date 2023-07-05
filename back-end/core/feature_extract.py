import os
import cv2

from core.utils.GLCM_feature import getGLCMFeatures
from core.utils.color_feature import color_moment
from core.utils.shape_feature import get_shape_fea
from core.utils.deep_feature import get_deep_fea
from core.utils.preproecss import proprocess
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity, pairwise_distances_chunked, pairwise_distances


# def get_cos_similar(v1, v2):
#     num = float(np.dot(v1, v2))  # 向量点乘
#     denom = np.linalg.norm(v1) * np.linalg.norm(v2)  # 求模长的乘积
#     return 0.5 + 0.5 * (num / denom) if denom != 0 else 0


# 图像预处理
def feature_extract():
    image_path = "/Users/rune/PycharmProjects/Flask-VUE/back-end/dataset/image_processed"
    print("开始预处理")
    image_list = [os.path.join(image_path, p) for p in os.listdir(image_path)]
    print(f"总共读取到{len(image_list)}张图片")

    image_list = image_list[:]

    # print("开始获取纹理特征")
    # GLCM_feature = [getGLCMFeatures(path) for path in tqdm(image_list)]
    # print("纹理数据获取完成")

    # print("开始获取颜色特征")
    # color_feature = np.load("/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/color.npy")
    # print("颜色数据获取完成")

    print("开始获取形状特征")
    shape_feature = np.array([get_shape_fea(path) for path in tqdm(image_list)])
    # shape_feature = np.load("/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/shape.npy")
    print("形状数据获取完成")

    # print("开始获取深度学习特征")
    # deep_feature = get_deep_fea(image_list)
    # deep_feature = np.load("/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/deep.npy")
    # print("深度学习数据获取完成")

    # np.save("/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/shape.npy", shape_feature)
    # exit(0)

    # print(shape_feature.shape)
    # pca = PCA(n_components=128)
    # new_shape_feature = pca.fit_transform(shape_feature)
    # print(new_shape_feature.shape)

    np.save("/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/shape.npy", shape_feature)

    exit(0)
    # mtx = pairwise_distances(deep_feature, deep_feature)
    #
    # for i in range(1000): mtx[i][i] = 1e6
    #
    # for i in range(1000):
    #     idx_lis = np.argsort(mtx[i])
    #
    #     img0 = cv2.imread(image_list[i])
    #     img1 = cv2.imread(image_list[idx_lis[0]])
    #     img2 = cv2.imread(image_list[idx_lis[1]])
    #     img3 = cv2.imread(image_list[idx_lis[2]])
    #     img4 = cv2.imread(image_list[idx_lis[3]])
    #     cv2.imshow('img0', img0)
    #     cv2.imshow('result1', img1)
    #     cv2.imshow('result2', img2)
    #     cv2.imshow('result3', img3)
    #     cv2.imshow('result4', img4)
    #     cv2.waitKey()


GLCM_feature = np.load(
    "/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/GLCM.npy")
color_feature = np.load(
    "/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/color.npy")
shape_feature = np.load(
    "/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/shape.npy")
deep_feature = np.load("/Users/rune/PycharmProjects/Flask-VUE/back-end/feature_dataset/deep.npy")


def Search_img(path, typ):
    global mtx, now_deep_fea, now_color_fea, now_shape_fea, now_GLCM_fea
    image_path = "/Users/rune/PycharmProjects/Flask-VUE/back-end/dataset/image_data"

    image_list = [p for p in os.listdir(image_path)]

    new_path = proprocess(path)

    if typ == 'E': now_deep_fea = get_deep_fea([new_path])
    if typ == 'A' or typ == 'D': now_color_fea = np.array([color_moment(new_path)])
    if typ == 'C' or typ == 'D': now_shape_fea = np.array([get_shape_fea(new_path)])
    if typ == 'B' or typ == 'D': now_GLCM_fea = np.array([getGLCMFeatures(new_path)])

    if typ == 'E': mtx = pairwise_distances(now_deep_fea, deep_feature)
    if typ == 'A': mtx = pairwise_distances(now_color_fea, color_feature)
    if typ == 'C': mtx = pairwise_distances(now_shape_fea, shape_feature)
    if typ == 'B': mtx = pairwise_distances(now_GLCM_fea, GLCM_feature)

    if typ == 'D':
        mtx1 = pairwise_distances(now_color_fea, color_feature)
        mtx2 = pairwise_distances(now_shape_fea, shape_feature)
        mtx3 = pairwise_distances(now_GLCM_fea, GLCM_feature)
        idx_lis = np.argsort(mtx1[0] + mtx2[0] + mtx3[0])
        result = [image_list[idx_lis[i]] for i in range(5)]
        print(result)
        return result

    # mtx = pairwise_distances(now_fea, deep_feature)

    idx_lis = np.argsort(mtx[0])
    result = [image_list[idx_lis[i]] for i in range(5)]

    print(result)
    return result


if __name__ == '__main__':
    path = "/Users/rune/PycharmProjects/Flask-VUE/back-end/uploads/tiger.png"

    Search_img(path, 'E')
