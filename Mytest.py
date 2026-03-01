from Mytrain import data_yaml_path
from ultralytics import YOLO

if __name__ == "__main__":
    # Load a model
    pth_path = r"D:\\GoogleDownloads\\Yun2\\ultralytics-main\\runs\\detect\\YOLO11s-RTTS-third\\weights\\best.pt"
    # model = YOLO('yolov8n.pt')  # load an official model
    model = YOLO(pth_path)  # load a custom model

    # Validate the model
    metrics = model.val(data='D:\\GoogleDownloads\\Yun2\\ultralytics-main\\ultralytics\\cfg\\datasets\\TGRS.yaml')  # no arguments needed, dataset and settings remembered
    metrics.box.map  # map50-95
    metrics.box.map50  # map50
    metrics.box.map75  # map75
    metrics.box.maps  # a list contains map50-95 of each category