from pathlib import Path
import json
import itertools

import tqdm
from easydict import EasyDict as edict
from PIL import Image

image_dir = r'D:\dataset\words\words\images'
json_file = r'D:\dataset\words\words\det_dataset.json'   # xmin, ymin, xmax, ymax
save_dir = r'D:\dataset\words\words\labels'

image_dir = Path(image_dir)
save_dir = Path(save_dir)

save_dir = Path(save_dir)
save_dir.mkdir(exist_ok=True)


json_data = json.load(open(json_file, encoding='utf-8'))


json_data_list = tqdm.tqdm(json_data.items())

# 0 代表行， 1代表word
for k, v in json_data_list:
    filename = Path(str(k)).name
    save_path = save_dir / filename.replace('.jpg', '.txt')

    labels_lines = v[0]
    labels_words = v[1]

    tmp = []
    for item in labels_words:
        tmp += item
    labels_words = tmp

    labels_ = []
    for item in labels_lines:
        xyxy = list(map(int, item[:4]))
        label = [0] + xyxy
        labels_.append(label)
    for item in labels_words:
        xyxy = list(map(int, item[:4]))
        label = [1] + xyxy
        labels_.append(label)

    # xyxy to xywh and norm
    labels_txt_list = []
    for label in labels_:
        c, xmin, ymin, xmax, ymax = label
        img = Image.open(image_dir / filename)
        img_w, img_h = img.size
        w = xmax - xmin
        h = ymax - ymin
        x = (xmax + xmin) / 2
        y = (ymax + ymin) / 2
        x /= img_w
        y /= img_h
        w /= img_w
        h /= img_h
        txt = f'{c} {x:.6f} {y:.6f} {w:.6f} {h:6f}\n'
        labels_txt_list.append(txt)

    with save_path.open('w') as f:
        f.writelines(labels_txt_list)
