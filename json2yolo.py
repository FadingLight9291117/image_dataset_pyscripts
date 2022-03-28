from pathlib import Path
import json

from easydict import EasyDict as edict

json_file = './test.json'
save_dir = 'test_labels'

save_dir = Path(save_dir)
save_dir.mkdir(exist_ok=True)


json_data = json.load(open(json_file))

for label in json_data:
    label = edict(label)
    image_path = Path(label.image_path)
    image_name = image_path.stem
    save_name = image_name + '.txt'
    boxes = label.boxes
    box_txt = ''
    for box in boxes:
        box = [f'{x:.6f}' for x in box]
        box_txt += '0 ' + ' '.join(box)
        box_txt += '\n'

    with save_dir.joinpath(save_name).open('w') as f:
        f.write(box_txt)
