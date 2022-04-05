import csv
import json
from pathlib import Path
import argparse

import tqdm
from PIL import Image


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--yolo-images', type=str,
                        default='../WIDER_FACE/train', help='yolo数据集文件夹')
    parser.add_argument('--yolo-labels', type=str,
                        default='../WIDER_FACE/train', help='yolo数据集文件夹')
    parser.add_argument('-c', '--coco', type=str,
                        default='../WIDER_FACE/train/annotations/labels.json', help='coco json file')
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    args = get_args()

    json_file = Path(args.coco)

    yolo_label_dir = Path(args.yolo_labels)
    yolo_image_dir = Path(args.yolo_images)

    assert (
        yolo_image_dir.exists() and
        yolo_image_dir.exists() and
        json_file.exists()
    ), "某个文件不存在！！！"

    labels = []
    for file in yolo_label_dir.glob('*'):

        image_name = file.stem + '.jpg'
        image_path = yolo_image_dir / image_name
        img = Image.open(image_path)
        img_w, img_h = img.size
        with file.open() as f:
            f_data = f.readlines()
        for line in f_data:
            c, x, y, w, h = list(map(float, line.strip().split()))
            x *= img_w
            y *= img_h
            w *= img_w
            h *= img_h
            c, x, y, w, h = list(map(int, [c, x, y, w, h]))
            labels.append([x, y, w, h, c, image_path.name])

    with json_file.open() as f:
        json_data = json.load(f)

    images = json_data['images']
    images = [
        {
            'id': item['id'],
            'filename': Path(item['file_name']).name
        }
        for item in images
    ]
    categories = json_data['categories']

    annos = []
    labels = tqdm.tqdm(labels)
    for idx, label in enumerate(labels):
        x, y, w, h, c, filename = label
        x, y, w, h, c = list(map(int, [x, y, w, h, c]))
        x1 = x - w // 2
        y1 = y - h // 2
        anno = {
            'id': idx,
            "image_id": None,
            "category_id": c,
            'area': w * h,
            'bbox': [x1, y1, w, h],
            'iscrowd': 0,
        }
        for image in images:
            if image['filename'] == filename:
                anno['image_id'] = image['id']

        annos.append(anno)

    json_data['annotations'] = annos

    with json_file.open('w') as f:
        json.dump(json_data, f)
