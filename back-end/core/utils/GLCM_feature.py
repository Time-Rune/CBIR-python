import cv2
from skimage.feature import graycomatrix, graycoprops
import numpy as np


def getGLCMFeatures(imgFilePath):
    # Load the image
    img = cv2.imread(imgFilePath)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    graycom = graycomatrix(gray, [1], [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256)

    # Find the GLCM properties
    contrast = graycoprops(graycom, 'contrast')
    dissimilarity = graycoprops(graycom, 'dissimilarity')
    homogeneity = graycoprops(graycom, 'homogeneity')
    energy = graycoprops(graycom, 'energy')
    correlation = graycoprops(graycom, 'correlation')
    ASM = graycoprops(graycom, 'ASM')

    feature = np.concatenate((contrast, dissimilarity, homogeneity, energy, correlation, ASM), axis=1)
    return feature.flatten()
