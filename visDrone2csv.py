import argparse
from pathlib import Path
import csv
from typing import List

from torch import save


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--origin', type=str,
                        default='../VisDrone/VisDrone2019-DET-train/annotations', help='VisDrone标签文件夹')
    parser.add_argument('-t', '--target', type=str,
                        default='./annos.csv', help='save path')
    args = parser.parse_args()

    return args


def txt2whboxes(txt_list: List[str]):
    boxes = []
    for txt in txt_list:
        txt_list = txt.strip().split(',')
        res = txt_list[:4] + txt_list[5:6]
        x1, y1, w, h = list(map(int, res[:4]))
        x = x1 + w // 2
        y = y1 + h // 2
        res[0] = x
        res[1] = y
        c = res[4]
        boxes.append([*res[:4], c])
    return boxes


def save2csv(save_path: Path, data:  list, header: list):
    with save_path.open('w', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(data)


if __name__ == '__main__':
    args = get_args()
    origin_dir = Path(args.origin)
    save_path = Path(args.target)
    annos = []
    for file in origin_dir.glob('*.txt'):
        txt_list = file.open().readlines()
        boxes = txt2whboxes(txt_list)
        for box in boxes:
            x, y, w, h, c = box
            anno = [x, y, w, h, c]
            filename = file.stem + '.jpg'
            anno.append(filename)
            annos.append(anno)

    hearder = ['x', 'y', 'w', 'h', 'c', 'filename']
    save2csv(save_path, annos, hearder)
