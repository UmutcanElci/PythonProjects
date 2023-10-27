from ultralytics import YOLO

model = YOLO("yolov8s.pt")

model.predict(source="img/1.jpg",save=True,conf=0.5,save_txt=True)