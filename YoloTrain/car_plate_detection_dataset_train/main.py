from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("../YOLO_Weights/yolov8n.pt")
    results = model.train(data="config.yaml", epochs=1)
