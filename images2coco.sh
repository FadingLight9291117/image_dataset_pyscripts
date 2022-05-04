base_dir=/media/clz/Work/dataset/words/words

python images2coco.py  ${base_dir}/train/images/ ${base_dir}/label.txt train.json
python images2coco.py  ${base_dir}/val/images/ ${base_dir}/label.txt val.json