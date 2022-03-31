from pathlib import Path

from show_whbox_from_yolo_txt import show_whbox_from_yolo_txt

import click


@click.command()
@click.option('--img-dir', type=str, default='...')
@click.option('--label-dir', type=str, default='...')
def show_whbox_from_yolo_dir(img_dir, label_dir):
    img_dir = Path(img_dir)
    label_dir = Path(label_dir)
    img_path_list = img_dir.glob('*.jpg')
    for img_path in img_path_list:
        label_name = img_path.stem + '.txt'
        label_path = label_dir / label_name
        if not label_path.exists():
            continue
        show_whbox_from_yolo_txt(img_path, label_path)
        input()
        
    
if __name__ == '__main__':
    show_whbox_from_yolo_dir()
