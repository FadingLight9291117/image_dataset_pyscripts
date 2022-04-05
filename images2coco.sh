base_dir=/media/clz/Work/dataset/widerface

python images2coco.py  ${base_dir}/images/train/ ${base_dir}/label.txt train.json
python images2coco.py  ${base_dir}/images/val/ ${base_dir}/label.txt val.json