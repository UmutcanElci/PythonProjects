from ultralytics import YOLO
from ultralytics.models.yolo.detect.predict import DetectionPredictor

from ultralytics.trackers.byte_tracker import BaseTrack
model = YOLO("yolov8x.pt")

results = model.predict(source="0",show=True)


print(results)