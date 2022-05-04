import csv
from pathlib import Path
import argparse

import tqdm
from PIL import Image


# csv: x, y, w, h (全像素), c, filename

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--origin', type=str,
                        default='../VisDrone/train/', help='VisDrone标签文件夹')
    parser.add_argument('-t', '--target', type=str,
                        default='../VisDrone/train/labels', help='save path')
    args = parser.parse_args()

    return args

def save_label(save_path: Path, lines: list):
    with save_path.open('w') as f:
        txt = '\n'.join(lines)
        f.write(txt)

if __name__ == '__main__':
    args = get_args()
    origin_dir = Path(args.origin)
    save_path = Path(args.target)
    save_path.mkdir(exist_ok=True, parents=True)

    images_dir = origin_dir / 'images'
    csv_path = list(origin_dir.glob('*.csv'))[0]
    

    with csv_path.open() as f:
        f_csv = csv.reader(f)
        csv_data = list(f_csv)[1:]

    anno_dict = {}
    csv_data = tqdm.tqdm(csv_data)
    for anno in csv_data:
        x, y, w, h, c, filename = anno
        v = anno_dict.setdefault(filename, [])
        
        im = Image.open(images_dir / filename)
        im_w, im_h = im.size
        x, y, w, h = [int(i) for i in [x, y, w, h]]
        x = x / im_w
        y = y / im_h
        w = w / im_w
        h = h / im_h
        label_txt = f'{c} {x:.6f} {y:.6f} {w:.6f} {h:6f}'
        v.append(label_txt)
    
    for k, v in anno_dict.items():
        file_path = save_path / k.replace('.jpg', '.txt')
        save_label(file_path, v)
    