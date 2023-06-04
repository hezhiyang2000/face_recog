_base_ = ["/home/hezy/projects/mmpose/configs/body_2d_keypoint/rtmpose/coco/rtmpose-s_8xb256-420e_coco-256x192.py"]

# dataset prepare

data_root = '/home/hezy/projects/triangle/data/Triangle_215_Keypoint_coco'
dataset_info = {
    'dataset_name':'Triangle_215_Keypoint_coco',
    'classes':'sjb_rect',
    'paper_info':{
        'author':'Tongji Zihao',
        'title':'Triangle Keypoints Detection',
        'container':'OpenMMLab',
        'year':'2023',
        'homepage':'https://space.bilibili.com/1900783'
    },
    'keypoint_info':{
        0:{'name':'angle_30','id':0,'color':[255,0,0],'type': '','swap': ''},
        1:{'name':'angle_60','id':1,'color':[0,255,0],'type': '','swap': ''},
        2:{'name':'angle_90','id':2,'color':[0,0,255],'type': '','swap': ''}
    },
    'skeleton_info': {
        0: {'link':('angle_30','angle_60'),'id': 0,'color': [100,150,200]},
        1: {'link':('angle_60','angle_90'),'id': 1,'color': [200,100,150]},
        2: {'link':('angle_90','angle_30'),'id': 2,'color': [150,120,100]}
    }
}

NUM_KEYPOINTS = len(dataset_info['keypoint_info'])
dataset_info['joint_weights'] = [1.0] * NUM_KEYPOINTS
dataset_info['sigmas'] = [0.025] * NUM_KEYPOINTS

ann_file_train = '/home/hezy/projects/triangle/data/Triangle_215_Keypoint_coco/train_coco.json'
ann_file_val = '/home/hezy/projects/triangle/data/Triangle_215_Keypoint_coco/val_coco.json'
data_prefix = 'images/'

# dataset settings
# 1. data directory set
# 2. dataset metainfo set

train_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        ann_file=ann_file_train,
        data_prefix=dict(img=data_prefix),
        metainfo=dataset_info, 
    ))
val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        ann_file=ann_file_val,
        data_prefix=dict(img=data_prefix),
        metainfo=dataset_info, 
    ))

val_evaluator = dict(
    type='CocoMetric',
    ann_file=ann_file_val)
test_evaluator = val_evaluator

# model settings
# change model output set. 

model = dict(
    head=dict(
        out_channels=NUM_KEYPOINTS))


