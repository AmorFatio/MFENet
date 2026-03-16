from ultralytics import YOLO

# 模型配置文件
model_yaml_path = "/ultralytics/cfg/models/MFENet\\MFENet.yaml"

# 数据集配置文件\
data_yaml_path = 'E:\\MFENet\\ultralytics\\cfg\\datasets\\RTTS.yaml'

if __name__ == '__main__':
    # 加载预训练模型
    model = YOLO(model_yaml_path)
    # 训练模型
    results = model.train(data=data_yaml_path, epochs=300, device=0, batch=16, resume=True, name='YOLO11s-OAWN-self', amp=False)

