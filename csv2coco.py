from fileinput import filename
from operator import contains
from pathlib import Path
import csv
import json
import argparse

import tqdm

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--json-file', type=str,
                        default='/media/clz/Work/dataset/VisDrone/train/annotations/label.json', help='生成的coco标签json文件')
    parser.add_argument('--csv-file', type=str,
                        default='/media/clz/Work/dataset/VisDrone/train/annos.csv', help='csv标签文件')

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    json_file = Path(args.json_file)
    csv_file = Path(args.csv_file)

    with csv_file.open() as f:
        f_csv = csv.reader(f)
        csv_data = list(f_csv)[1:]

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
    csv_data = tqdm.tqdm(csv_data)
    for idx, label in enumerate(csv_data):
        x, y, w, h, c, filename = label
        if c == '0':
            continue
        x, y, w, h, c = list(map(int, [x, y, w, h, c]))
        x1 = x - w // 2
        y1 = y - h // 2
        anno = {
            'id': idx,
            "image_id": None,
            "category_id": c,
            'area': w * h,
            'bbox': [x1, y1, w, h],
        }
        for image in images:
            if image['filename'] == filename:
                anno['image_id']  = image['id']
    
        annos.append(anno)
    
    json_data['annotations'] = annos
    
    with json_file.open('w') as f:
        json.dump(json_data, f)