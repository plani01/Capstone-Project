import cv2
import os
from time import sleep
from stopwatch import Stopwatch
from datetime import datetime

#video capture object
cap = cv2.VideoCapture(0)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

#print("frame width: ", frame_width, "\n")
#print("frame height: ", frame_height, "\n")

video_Dir_name = "lighterImages2"
IsDirExist = os.path.exists(video_Dir_name)
if not IsDirExist:
        os.mkdir(video_Dir_name)



#Saving video frames as video 
#out = cv2.VideoWriter( "videoOutput/" + timeStr + ".avi",cv2.VideoWriter_fourcc('M','J','P','G'), 5, (frame_width,frame_height))

fileNumber = 0

while(cap.isOpened):

    sleep(0.5)

    _, frame = cap.read()

    cv2.imshow("frame", frame)

    cv2.imwrite(video_Dir_name+"/img"+str(fileNumber)+".jpg", frame)

    fileNumber += 1

    #out.write(frame)



    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("0: this is a success")