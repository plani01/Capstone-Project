#import torch
import numpy as np
import cv2
#from super_gradients.common.object_names import Models
from super_gradients.training import models

model = models.get('yolo_nas_s', num_classes=2, checkpoint_path="C:/Users/plani/Documents/Design2 Models/small_ckpt_best.pth")
#model.predict_webcam()

cap = cv2.VideoCapture(0)

while(cap.isOpened):
    _, frame = cap.read()

    outputs = model.predict(frame)
    # Get bounding boxes: 
    prediction_objects = list(outputs._images_prediction_lst)[0]
    bbox_floats = prediction_objects.prediction.bboxes_xyxy
    if len(bbox_floats) == 0:
        go = 0
    else:
        go = 1
        rounded_int_list = [int(round(x)) for x in bbox_floats[0]]
        bbox = tuple(np.array(rounded_int_list, dtype='int')) 
        cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255,0,0), 3)
    # Convert floats to int
    
    cv2.imshow('frame', frame)
    print("GO: ", go)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# img = cv2.imread("C:/Users/plani/Documents/Design2 Pics/webCam Pics/lighterImages/img21.jpg")
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# outputs = model.predict(img)
# #print(outputs)
# prediction_objects = list(outputs._images_prediction_lst)[0]
# bbox_floats = prediction_objects.prediction.bboxes_xyxy
# rounded_int_list = [int(round(x)) for x in bbox_floats[0]]
# bbox = tuple(np.array(rounded_int_list, dtype='int')) 
# cv2.rectangle(img, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255,0,0), 3)
# cv2.imshow('frame', img)

# # print("outputs[0] type", type(outputs[0]))
# # print("outputs[0]", outputs[0])


# #print(bbox)
# #outputs.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()