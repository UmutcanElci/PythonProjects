from ultralytics import YOLO
import cv2

cap=cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))


#output = cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc("M","J","P","G"),10,(frame_width,frame_height))

model = YOLO("../YOLO_Weights/yolov8n.pt")

while True:
    succes, img = cap.read()
    results = model(img,stream=True)
    
    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,0),2)
    cv2.imshow("Image",img)
    if cv2.waitKey(1) & 0xff== ord("1"):
       break






