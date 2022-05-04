base_dir=/media/clz/Work/dataset/words/words

python yolo2coco.py \
--coco ${base_dir}/annotations/train.json \
--yolo-images ${base_dir}/train/images \
--yolo-labels ${base_dir}/train/labels

python yolo2coco.py \
--coco ${base_dir}/annotations/val.json \
--yolo-images ${base_dir}/val/images \
--yolo-labels ${base_dir}/val/labels