import os
# from pycocotools.coco import COCO
from tqdm import tqdm


if __name__ == "__main__":
    tar_dir = '/shared/xudongliu/bdd100k/100k/train/'
    ref_dir = '/shared/xudongliu/bdd100k/labels/voc_val/class_labels/'
    fns = os.listdir(tar_dir)
    ref_fns = os.listdir(ref_dir)
    ref_name = [fn.split('.')[0] for fn in ref_fns]
    for fn in tqdm(fns):
        if fn.split('.')[0] not in ref_name:
            os.remove(os.path.join(tar_dir, fn))
            print(fn)
            break