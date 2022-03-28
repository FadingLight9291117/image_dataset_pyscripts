import shutil
import json
from pathlib import Path

from PIL import Image


def process_label(label_txt, image_dir):
    txt_list = open(label_txt).readlines()
    size = len(txt_list)

    labels = []

    i = 0
    while i < size:
        image_path = txt_list[i].strip()

        imagePath = Path(image_dir) / image_path

        img_w, img_h = Image.open(imagePath).size

        face_num = int(txt_list[i+1])
        i += 2
        if face_num == 0:
            label = dict(
                image_path=image_path,
                n=0,
                boxes=[],
            )
            i += 1
        else:
            boxes = []
            for f in txt_list[i:i+face_num]:
                f = f.strip().split()[:4]
                f = list(map(float, f))
                x1, y1, w, h = f
                x = x1 + w // 2
                y = y1 + h // 2
                x /= img_w
                w /= img_w
                y /= img_h
                h /= img_h
                boxes.append([x,y,w,h])

            label = dict(
                image_path=image_path,
                image_size=[img_w, img_h],
                n=face_num,
                boxes=boxes,
            )
            i += face_num

        labels.append(label)

    return labels


if __name__ == '__main__':
    wider_images_path = '/media/clz/Work/dataset/widerface/WIDER_val/WIDER_val/images'
    wider_label_path = '/media/clz/Work/dataset/widerface/wider_face_split/wider_face_split/wider_face_val_bbx_gt.txt'
    labels = process_label(wider_label_path, wider_images_path)

    save_path = './label.json'
    with open(save_path, 'w') as f:
        json.dump(labels, f)
