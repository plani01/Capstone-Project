import cv2
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras

modelOld = tf.keras.models.load_model("C:/Users/plani/Documents/Design2 Models/Aug_MLP_CNN.keras")
#modelNew = tf.keras.models.load_model("C:/Users/plani/Documents/Design2 Models/Aug_MLP_CNN2.keras")

#print(modelOld.summary())

cap = cv2.VideoCapture(0)

while(cap.isOpened):

    _, frame = cap.read()

    frame = cv2.resize(frame, dsize = (300, 300), interpolation=cv2.INTER_CUBIC)
    frame = np.reshape(frame,(1,300,300,3))
    cv2.imshow('frame', frame[0])
    

    #print(frame.shape)
    prediction = np.argmax(modelOld.predict(frame),axis=1)
    print( "Detecting class: ", prediction)

    if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()



print("succesfully ran: program is over")