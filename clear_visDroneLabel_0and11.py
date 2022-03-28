import argparse
from ast import parse

from pathlib import Path


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, default='', help='标签文件夹')

    args = parser.parse_args()

    return args


def clear_label(txt_path: Path):
    with txt_path.open() as f:
        lines = f.readlines()

    lines = list(filter(lambda line: not line.startswith(
        '0') and not line.startswith('11'), lines))

    with txt_path.open('w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    args = get_args()

    path = Path(args.path)
    for txt_path in path.glob('*'):
        clear_label(txt_path)
