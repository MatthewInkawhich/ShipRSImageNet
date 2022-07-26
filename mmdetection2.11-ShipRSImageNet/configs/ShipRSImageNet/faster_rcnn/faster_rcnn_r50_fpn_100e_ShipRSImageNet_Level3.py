_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/ShipRSImageNet_Level3_detection.py',
    '../_base_/schedules/schedule_100e.py', '../_base_/default_runtime.py',
]


model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=50))
    )


evaluation = dict(interval=50, metric='bbox')

work_dir='./out/ShipRSImageNet/logs/faster_rcnn/faster_rcnn_r50_fpn_100e_ShipRSImageNet_Level3'
