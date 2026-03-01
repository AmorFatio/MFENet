
from ultralytics import YOLO

if __name__ == '__main__':

    # Load a model
    model = YOLO(model=r'D:\\GoogleDownloads\\Yun2\\ultralytics-main\\runs\\detect\\YOLO11s-OAWN-self12\\weights\\best.pt')
    model.predict(source=r'D:\GoogleDownloads\Yun2\ultralytics-main\ultralytics\cfg\datasets\Fig1',
                  save=True,
                  show=False,
                  )

