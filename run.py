from coco2voc import *
from PIL import Image


if __name__ == '__main__':
    # !!Change paths to your local machine!!
    annotations_file = '/shared/xudongliu/bdd100k/labels/bdd100k_labels_images_det_coco_val.json'
    labels_target_folder = '/shared/xudongliu/bdd100k/labels/voc_val'
    # data_folder = '/home/dl/1TB-Volumn/MSCOCO2017/train2017'


    # Convert n=25 annotations
    coco2voc(annotations_file, labels_target_folder, compress=True)