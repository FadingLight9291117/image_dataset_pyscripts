from pathlib import Path
import shutil
import os


def trans(img_dir, images: list):
    img_dir = Path(img_dir)
    for item in img_dir.glob('*'):
        if item.is_file():
            images.append(item.absolute())
        if item.is_dir():
            trans(item, images)
    return images


image_dir = '/media/clz/Work/dataset/widerface/WIDER_val'

save_dir = './val_images'

label_txt = './val.txt'

save_dir = Path(save_dir)
save_dir.mkdir(exist_ok=True)

images = []

images = trans(image_dir, images)

txt = []
for image in images:
    shutil.copy(image, save_dir / image.name)
    txt.append(image.name + '\n')

txt = sorted(txt)
    
with open(label_txt, 'w') as f:
    f.writelines(txt)