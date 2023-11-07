import matplotlib.pyplot as plt
import numpy as np
from ultralytics import YOLO
import supervision as sv
from IPython import display
polygon = np.array([
    [770, 400], #l1
    [420, 610], #l2
    [1250, 970], #l3
    [1540, 660] #l4
])

model = YOLO("yolov8m.pt")

video_info = sv.VideoInfo.from_video_path("1.mp4")
zone = sv.PolygonZone(polygon=polygon,frame_resolution_wh=video_info.resolution_wh)


box_annotator = sv.BoxAnnotator(thickness=2,text_thickness=1,text_scale=1)
zone_annotator = sv.PolygonZoneAnnotator(zone=zone,color=sv.Color.white(), thickness=3, text_thickness=3, text_scale=2)


def process_frame(frame: np.ndarray, _)-> np.ndarray:
    results = model(frame, imgsz=1280)[0]
    detections = sv.Detections.from_ultralytics(results)
    detections = detections[detections.class_id == 0]
    zone.trigger(detections=detections)
    
    box_annotator = sv.BoxAnnotator(thickness=4, text_thickness=4, text_scale=2)
    labels = [f"{model.names[class_id]}: {confidence:.2f}" for class_id, confidence in zip(detections.class_id, detections.confidence)]
    frame = box_annotator.annotate(scene=frame, detections=detections, labels=labels)
    frame = zone_annotator.annotate(scene=frame)
    
    
    
    # Ekrana mesajı yazdır 
    return frame

sv.process_video(source_path="1.mp4", target_path="C:\\Users\\Malat\\Downloads\\result.mp4", callback=process_frame)

display.clear_output()
#plt.imshow(frame)
#plt.show()
#sv.plot_image(frame, (16, 16))