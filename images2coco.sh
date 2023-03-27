base_dir=/media/clz/Work/dataset/jiankong

python images2coco.py  ${base_dir}/train/images/ ${base_dir}/labels.txt train.json
python images2coco.py  ${base_dir}/val/images/ ${base_dir}/labels.txt val.json