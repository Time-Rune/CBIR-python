import cv2


def predict(dataset, model, ext):
    x = dataset[0].replace('\\', '/')
    file_name = dataset[1]
    print(x)
    print(file_name)
    x = cv2.imread(x)
    img_y, image_info = model.detect(x)
    cv2.imwrite('./tmp/draw/{}.{}'.format(file_name, ext), img_y)
    cv2.line(img_y, (0, 0), (300, 300), (0, 0, 255), 30)
    cv2.imwrite('./tmp/draw2/{}.{}'.format(file_name, ext), img_y)
    return image_info
