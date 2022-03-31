from pathlib import Path

from PIL import Image, ImageDraw
import click
from easydict import EasyDict as edict


def whbox2bbox(whbox,  imgW, imgH):
    x, y, w, h = whbox
    x *= imgW
    y *= imgH
    w *= imgW
    h *= imgH
    x1 = x - w / 2
    y1 = y - h / 2
    x2 = x + w / 2
    y2 = y + h / 2
    x1, y1, x2, y2 = list(map(int, [x1, y1, x2, y2]))
    return x1, y1, x2, y2


def draw1whbox(imgD: ImageDraw.ImageDraw, whbox, imgW, imgH):
    bbox = whbox2bbox(whbox, imgW, imgH)
    imgD.rectangle(bbox, outline='red')
    return imgD


# @click.command()
# @click.option('--img-path', type=str, default='...')
# @click.option('--txt-file', type=str, default='...')
def show_whbox_from_yolo_txt(img_path, txt_file):
    img_path = Path(img_path)
    txt_file = Path(txt_file)
    img = Image.open(img_path)
    imgW, imgH = img.size
    imgD = ImageDraw.ImageDraw(img)
    with txt_file.open() as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split()
        line = line[1:]
        whbox = list(map(float, line))
        imgD = draw1whbox(imgD, whbox, imgW, imgH)
    img.show()


if __name__ == '__main__':
    show_whbox_from_yolo_txt()