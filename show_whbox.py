from pathlib import Path
import argparse

from PIL import Image, ImageDraw


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, default='', help='image path')
    parser.add_argument('-b', '--box', type=str,
                        default='0.2 , 0.2, 0.5, 0.5', help='whbox')
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    args = get_args()
    path = Path(args.path)
    whbox = list(map(float, args.box.strip().split(',')))

    img = Image.open(path)

    w, h = img.size
    whbox[0] *= w
    whbox[1] *= h
    whbox[2] *= w
    whbox[3] *= h

    whbox = list(map(int, whbox))

    x, y, w, h = whbox

    x1 = x - w // 2
    x2 = x + w // 2
    y1 = y - h // 2
    y2 = y + h // 2

    imgD = ImageDraw.ImageDraw(img)
    imgD.rectangle((x1, y1, x2, y2), outline='red')
    img.show()
