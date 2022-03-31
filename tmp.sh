python yolo2coco.py \
--coco /media/clz/Work/dataset/VisDrone/annotations/train.json \
--yolo-images /media/clz/Work/dataset/VisDrone/train/images \
--yolo-labels /media/clz/Work/dataset/VisDrone/train/labels


python yolo2coco.py \
--coco /media/clz/Work/dataset/VisDrone/annotations/test.json \
--yolo-images /media/clz/Work/dataset/VisDrone/test/images \
--yolo-labels /media/clz/Work/dataset/VisDrone/test/labels

python yolo2coco.py \
--coco /media/clz/Work/dataset/VisDrone/annotations/val.json \
--yolo-images /media/clz/Work/dataset/VisDrone/val/images \
--yolo-labels /media/clz/Work/dataset/VisDrone/val/labels
