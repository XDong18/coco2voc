import os
from pycocotools.coco import COCO
from tqdm import tqdm


if __name__ == "__main__":
    tar_dir = '/shared/xudongliu/bdd100k/labels/voc_train/class_labels'
    coco_fn = '/shared/xudongliu/bdd100k/labels/bdd100k_labels_images_det_coco_train.json'
    coco = COCO(coco_fn)
    imgs = coco.imgs
    for img in tqdm(imgs):
        info = imgs[img]
        sur_fn = os.path.join(tar_dir, str(img) + '.png')
        des_fn = os.path.join(tar_dir, info['file_name'].split('.')[0] + '.png')
        os.rename(sur_fn, des_fn)
