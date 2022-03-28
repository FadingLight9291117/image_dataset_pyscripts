from email.mime import image
from pathlib import Path
import json
import argparse

from PIL import Image, ImageDraw


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--label-path', type=str,
                        default='/media/clz/Work/dataset/VisDrone/train/annotations/label.json', help='label file path')
    args = parser.parse_args()
    return args


def whbox2bbox(whbox):
    x, y, w, h = whbox
    x1 = x - w // 2
    x2 = x + w // 2
    y1 = y - h // 2
    y2 = y + h // 2

    return [x1, y1, x2, y2]


def draw_boxes(img, whboxes):
    img_w, img_h = img.size
    imgD = ImageDraw.ImageDraw(img)

    for whbox in whboxes:
        x1, y1, x2, y2= whbox
        x1, y1, x2, y2 = whbox2bbox([x1, y1, x2, y2])

        color = 'red'
        imgD.rectangle((x1, y1, x2, y2), outline=color)

    return img


if __name__ == '__main__':
    args = get_args()
    label_path = Path(args.label_path)

    with label_path.open() as f:
        json_data = json.load(f)

    images = json_data['images']
    for label in json_data['annotations']:
        image_id = label['image_id']
        bbox = label['bbox']
        
        x1, y1, w, h = list(map(int, bbox))
        x = x1 + w // 2
        y = y1 + h // 2
        
        for i in images:
            if i['id'] == image_id:
                image_path = i['file_name']
        
        image_path = Path(image_path)
        img = Image.open(image_path)
        img = draw_boxes(img, [[x, y, w, h]])
        
        img.show()
        
        input()
                
        
        
