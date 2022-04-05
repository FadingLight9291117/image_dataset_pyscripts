base_dir=/media/clz/Work/dataset/widerface

python yolo2coco.py \
--coco ${base_dir}/annotations/train.json \
--yolo-images ${base_dir}/images/train \
--yolo-labels ${base_dir}/labels/train

python yolo2coco.py \
--coco ${base_dir}/annotations/val.json \
--yolo-images ${base_dir}/images/val \
--yolo-labels ${base_dir}/labels/val