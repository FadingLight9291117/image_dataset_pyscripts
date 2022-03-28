from pathlib import Path
import argparse

from PIL import Image, ImageDraw


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str,
                        default='', help='image path')
    parser.add_argument('-l', '--label', type=str,
                        default='', help='label file path')
    args = parser.parse_args()
    return args


def read_label(path: Path):
    with path.open() as f:
        lines = f.readlines()
    lines = [line.split()[1:] + [line.split()[0]] for line in lines]
    lines = [list(map(float, line)) for line in lines]

    return lines


def draw_boxes(img, whboxes):
    img_w, img_h = img.size
    imgD = ImageDraw.ImageDraw(img)

    for whbox in whboxes:
        x1, y1, x2, y2, c = whbox
        x1, y1, x2, y2  = whbox2bbox([x1, y1, x2, y2])

        x1 *= img_w
        y1 *= img_h
        x2 *= img_w
        y2 *= img_h

        color = 'red'
        if c == 0:
            color = 'blue'
        imgD.rectangle((x1, y1, x2, y2), outline=color)

    return img


def whbox2bbox(whbox):
    x, y, w, h = whbox
    x1 = x - w / 2
    x2 = x + w / 2
    y1 = y - h / 2
    y2 = y + h / 2

    return [x1, y1, x2, y2]


if __name__ == '__main__':
    args = get_args()
    image_path = Path(args.image)
    label_path = Path(args.label)

    img = Image.open(image_path)

    lines = read_label(label_path)
    img = draw_boxes(img, lines)

    img.show()
