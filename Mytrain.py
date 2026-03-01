#coding:utf-8
from ultralytics import YOLO

# 模型配置文件
model_yaml_path = "D:\\GoogleDownloads\\Yun2\\ultralytics-main\\ultralytics\\cfg\\models\\11\\yolo11third.yaml"  #deaaze
# 数据集配置文件\
#data_yaml_path = 'D:\\GoogleDownloads\\ultralytics-main\\ultralytics-main\\ultralytics\\cfg\\datasets\\VOC.yaml'
data_yaml_path = 'D:\\GoogleDownloads\\Yun2\\ultralytics-main\\ultralytics\\cfg\\datasets\\TGRS.yaml'
#data_yaml_path = 'E:\\yolov10-main\\ultralytics\\cfg\\datasets\\Rtts.yaml'
# 预训练模型
#pre_model_name = '/home/jkj21202302198/Yun2/runs/detect/wu-SCAM35/weights/last.pt'
#E:\\yolov10-main\\yolov10n.pt
if __name__ == '__main__':
    # 加载预训练模型
    model = YOLO(model_yaml_path)
    # 训练模型
    results = model.train(data=data_yaml_path, epochs=300, device=0, batch=16, resume=True, name='YOLO11s-OAWN-self', amp=False)

