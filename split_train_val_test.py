from cProfile import label
import shutil
from pathlib import Path
import argparse
import random

import tqdm
from argon2 import DEFAULT_RANDOM_SALT_LENGTH
from pandas import cut

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img-dir', type=str, default='D:\dataset\words\words\images')
    parser.add_argument('--label-dir', type=str, default='D:\dataset\words\words\labels')
    parser.add_argument('--cut-point', type=float, default=0.8)
    
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    
    img_dir = Path(args.img_dir)
    label_dir = Path(args.label_dir)
    cut_point = args.cut_point
    
    img_paths = list(img_dir.glob('*.jpg'))
    
    size = len(list(img_paths))
    cut_point = int(size * cut_point)
    
    train_dir = img_dir.parent / 'train'
    val_dir = img_dir.parent / 'val'
    train_dir.mkdir(exist_ok=True)
    val_dir.mkdir(exist_ok=True)
    
    (train_dir / 'images').mkdir(exist_ok=True)
    (val_dir / 'images').mkdir(exist_ok=True)
    (train_dir / 'labels').mkdir(exist_ok=True)
    (val_dir / 'labels').mkdir(exist_ok=True)
    
    random.shuffle(img_paths)
    train_img_paths = list(img_paths)[:cut_point]
    val_img_paths = list(img_paths)[cut_point:]

    train_img_paths = tqdm.tqdm(train_img_paths)
    train_img_paths.set_description('split train')
    for img_path in train_img_paths:
        label_path = label_dir / (img_path.stem + '.txt')
        shutil.copy(img_path, train_dir / 'images')
        shutil.copy(label_path, train_dir / 'labels')
        # print(f'copy {img_path.name} and {label_path.name}')
    
    val_img_paths = tqdm.tqdm(val_img_paths)
    val_img_paths.set_description('split test')
    for img_path in val_img_paths:
        label_path = label_dir / (img_path.stem + '.txt')
        shutil.copy(img_path, val_dir / 'images')
        shutil.copy(label_path, val_dir / 'labels')
        # print(f'copy {img_path.name} and {label_path.name}')
        