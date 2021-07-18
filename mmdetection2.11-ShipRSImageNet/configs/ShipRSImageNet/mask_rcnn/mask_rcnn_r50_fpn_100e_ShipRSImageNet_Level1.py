_base_ = [
    '../_base_/models/mask_rcnn_r50_fpn.py',
    '../_base_/datasets/ShipRSImageNet_Level1_instance.py',
    '../_base_/schedules/schedule_100e.py', '../_base_/default_runtime.py',
]
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=4),
        mask_head=dict(
            num_classes=4)))

evaluation = dict(interval=2, metric=['bbox', 'segm'])