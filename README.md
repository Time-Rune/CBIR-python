# CBIR-python

## 摘要

本项目使用Vue+Flask架构实现了前后端分离的Web系统，通过特征提取和图像检索实现了以图搜图功能。通过对图像进行预处理，可以提高图像的可识别性。分别使用了颜色特征，形状特征，纹理特征以及ResNet和AutoEncoder等深度学习模型获得的深度学习特征，并使用PCA进行降维处理，提高了运行速度。通过评价标准mAP对不同特征的性能进行了测试，结果表明AutoEncoder特征的性能最好。项目还存在查询准确度低和页面功能不完善等问题，可以通过综合使用多种特征、改进深度学习模型和增加页面功能等方式进行改进。

关键词：Vue、Flask、特征提取、图像检索、深度学习、预处理、主成分分析