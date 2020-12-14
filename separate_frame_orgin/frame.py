from PIL import Image, ImageSequence
import config
import json
import os.path


def freme_func(img):
    try:
        img = Image.open(img)
    except IOError:
        print("Fail to open image")

    dic_list = []
    index = 0
    for frame in ImageSequence.Iterator(img):
        filename = str(index) + ".png"
        frame.save(os.path.join(config.BASE_DIR, 'picture/') + filename)
        dic = {"name": filename, "url": "http://172.16.60.192:8080" + os.path.join(config.BASE_DIR, 'picture/') + filename}
        dic_list.append(dic)
        index += 1

    # print(dic_list)
    with open('freme.json', 'w') as f:
        f.write(json.dumps(dic_list))


if __name__ == '__main__':
    freme_func("test.gif")
