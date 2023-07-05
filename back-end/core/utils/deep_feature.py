import numpy as np
import torch
from torchvision import models
import cv2
from tqdm import tqdm
from torch.utils.data import Dataset, DataLoader

resnet = models.resnet152(weights="ResNet152_Weights.IMAGENET1K_V1").to('mps')
means = np.array([103.939, 116.779, 123.68]) / 255.  # mean of three channels in the order of BGR


class IMDataLoader(Dataset):
    def __init__(self, lis):
        self.lis = lis

    def __len__(self):
        return len(self.lis)

    def __getitem__(self, item):

        img = cv2.resize(cv2.imread(self.lis[item]), (224, 224))
        img = np.transpose(img, (2, 0, 1)) / 255.0
        img[0] -= means[0]  # reduce B's mean
        img[1] -= means[1]  # reduce G's mean
        img[2] -= means[2]  # reduce R's mean
        img = np.expand_dims(img, axis=0)
        arr = torch.Tensor(img).to('mps')
        return arr


def get_deep_fea(image_list):
    siz = len(image_list)
    fea_arr = np.empty((siz, 1000))

    input = IMDataLoader(image_list)

    for i, data in tqdm(enumerate(input)):
        output = resnet(data)
        fea_arr[i] = output.cpu().detach().numpy()

    return fea_arr
