from IPython import display
from ultralytics import YOLO
from supervision import *

import numpy


model = YOLO("yolov8m.pt")
CLASS_NAMES_DICT = model.model.names#Takes yolov8m.pt model names
SOURCE_VIDEO = "YoloTry\\TrackCount\\vehicle-counting.mp4"
TARGET_VIDEO_PATH = "C:\\Users\\Malat\\Downloads\\vehicle-result.mp4"
video_info = VideoInfo.from_video_path(SOURCE_VIDEO)
box_annotator = BoxAnnotator(thickness=4,text_thickness=4,text_scale=2)


generator = get_video_frames_generator(SOURCE_VIDEO)




with VideoSink(TARGET_VIDEO_PATH,video_info) as sink:
    for frame in generator:
    
       results = model(frame)[0]
       
       detections = Detections(
           xyxy = results.boxes.xyxy.cpu().numpy(),
           confidence = results.boxes.conf.cpu().numpy(),
           class_id = results.boxes.cls.cpu().numpy().astype(int)
       )
       
       labels = [
           f"{CLASS_NAMES_DICT[class_id]} {confidence:0.2f}"
           for xyxy, confidence, class_id
           in zip(detections.xyxy, detections.confidence, detections.class_id)#same order
       ]
       
       frame = box_annotator.annotate(scene=frame,detections=detections,labels=labels)
       
       sink.write_frame(frame)