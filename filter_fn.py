import os
# from pycocotools.coco import COCO
from tqdm import tqdm


if __name__ == "__main__":
    tar_dir = '/shared/xudongliu/bdd100k/100k/train/'
    ref_dir = '/shared/xudongliu/bdd100k/labels/voc_train/class_labels/'
    fns = os.listdir(tar_dir)
    ref_fns = os.listdir(ref_dir)
    ref_name = [fn.split('.')[0] for fn in ref_fns]
    tar_name = [fn.split('.')[0] for fn in fns]
    diff = [x for x in tar_name if x not in ref_name]
    # print(diff)
    # print(len(diff))
    for fn in diff:
        os.remove(os.path.join(tar_dir, fn + '.jpg'))
    # print(ref_name[0])
    # for fn in tqdm(fns):
    #     if fn.split('.')[0] not in ref_name:
    #         os.remove(os.path.join(tar_dir, fn))
    #         print(fn, fn.split('.')[0])
    #         break