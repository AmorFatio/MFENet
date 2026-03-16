from ultralytics import YOLO

if __name__ == '__main__':

    # Load a model
    model = YOLO(model=r'..best.pt')
    model.predict(source=r'..fig.1',
                  save=True,
                  show=False,
                  )
