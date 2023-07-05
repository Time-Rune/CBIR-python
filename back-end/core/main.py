import os
import cv2


def pre_process(data_path):
    file_name = os.path.split(data_path)[1].split('.')[0]
    return data_path, file_name


def predict(dataset, model, ext):
    x = dataset[0].replace('\\', '/')
    file_name = dataset[1]
    print(x)
    print(file_name)
    x = cv2.imread(x)
    img_y = x
    image_info = {}
    cv2.imwrite('./tmp/draw/{}.{}'.format(file_name, ext), img_y)
    return image_info


def c_main(path, model, ext):
    image_data = pre_process(path)
    image_info = predict(image_data, model, ext)

    return image_data[1] + '.' + ext, image_info


if __name__ == '__main__':
    pass
