from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K

input_img = Input(shape=(28, 28, 1))
# encoder
# 创建第一个卷积层，过滤器个数为16，卷积核大小为3*3 --->（28，28，16）
x = Conv2D(16, (3, 3), activation='relu', padding='same')(input_img)
# 创建第一个池化层 ----->（14，14，16）
x = MaxPooling2D((2, 2), padding='same')(x)
# 第二个卷积层 ----->（14，14，8）
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
# 第二个池化层 ----->（7，7，8）
x = MaxPooling2D((2, 2), padding='same')(x)
# 第三个卷积层 ----->（7，7，8）
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
# 第三个池化层 ----->（4，4，8）
encoded = MaxPooling2D((2, 2), padding='same')(x)

# decoder
# 第一个卷积层 ----->（4，4，8）
x = Conv2D(8, (3, 3), activation='relu', padding='same')(encoded)
# 第一个upsampling层 ----->（8，8，8）
x = UpSampling2D((2, 2))(x)
# 第二个卷积层 ----->（8，8，8）
x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
# 第二个upsampling层 ----->（16，16，8）
x = UpSampling2D((2, 2))(x)
# 第三个卷积层 ----->（14，14，16）
x = Conv2D(16, (3, 3), activation='relu')(x)
# 第三个upsampling层 ----->（28，28，8）
x = UpSampling2D((2, 2))(x)
# 第四个卷积层 ----->（28，28，1）
decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
