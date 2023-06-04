# inherit directly from predefined config and change only what we need
_base_ = '/home/hezy/projects/mmdetection/configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py'

# model config:
# 1. change the roi head to only recognize triangle
# 2. set the model pretrain path
model = dict(
    roi_head = dict(
        bbox_head = dict(num_classes=1)))

# load_from='pretrained/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
# resume=False

# dataset config: change coco to our triangle dataset
# Need to do:
# 1. change metadata in train and test datasets. 
#    Because our dataset only have one category
# 2. change data root directory
# 3. add a valuation metric VOCMetric

data_root = '/home/hezy/projects/triangle/data/Triangle_215_Keypoint_coco/'
train_ann_file = 'train_coco.json'
val_ann_file = 'val_coco.json'
data_prefix = 'images/'
metainfo = {'classes': ('sjb_rect', )}

train_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        ann_file=train_ann_file,
        data_prefix=dict(img=data_prefix),
        metainfo=metainfo))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        ann_file=val_ann_file,
        data_prefix=dict(img=data_prefix),
        metainfo=metainfo))

val_evaluator = [
    dict(type='CocoMetric',ann_file=data_root + 'val_coco.json'), 
    dict(type='VOCMetric', metric='mAP', eval_mode='11points')
]

test_evaluator = val_evaluator

