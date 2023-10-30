from ultralytics import YOLO
import cv2

model = YOLO("../YOLO_Weights/yolov8n.pt")
results = model("../img/traffic.jpeg", show=True)


cv2.waitKey(0)
