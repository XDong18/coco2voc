import os
from pycocotools.coco import COCO
from tqdm import tqdm


if __name__ == "__main__":
    tar_dir = '/shared/xudongliu/bdd100k/labels/voc_val'
    coco_fn = '/shared/xudongliu/bdd100k/labels/bdd100k_labels_images_det_coco_val.json'
    coco = COCO(coco_fn)
    imgs = coco.imgs
    for img in tqdm(imgs):
        sur_fn = os.path.join(tar_dir, str(img) + '.png')
        des_fn = os.path.join(tar_dir, img['file_name'].split('.')[0] + '.png')
        os.rename(sur_fn, des_fn)
