import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET # reads xml bounding box annotation 
import os 
import cv2
import dill
import time
from stopwatch import Stopwatch

dill_filename = "SVM_classify.pkl"
with open(dill_filename, 'rb') as file:
    svm_model = dill.load(file)

stopwatchLoop = Stopwatch(2)
stopwatchFrameProcessing = Stopwatch(2)
stopwatchPrediction = Stopwatch(2)
vid = cv2.VideoCapture(0)
while(True):
    stopwatchLoop.start()
    _, frame = vid.read()
    #fileFrame = cv2.imwrite("exampleFrame.jpg",frame)
    
    newFrame = cv2.resize(frame, dsize = (300, 300), interpolation=cv2.INTER_CUBIC)
    #cv2.imshow('frame', newFrame)
    # Display the resulting frame
    #newFrame = cv2.imread("exampleFrame.jpg")
    stopwatchFrameProcessing.start()
    framePixels = np.array(newFrame)

    # Resizes 300x300 image to 90,000x1 array
    #print(framePixels.size)
    preprocessedFrame = framePixels.ravel()[np.newaxis,:]
    #print(preprocessedFrame)
    preprocessedFrame = preprocessedFrame/255
    #print(preprocessedFrame.size)
    stopwatchFrameProcessing.stop()
    stopwatchPrediction.start()
    test = svm_model.predict(preprocessedFrame)
    stopwatchPrediction.stop()
    stopwatchLoop.stop()
    print('Total time for whole loop: ' + str(stopwatchLoop.duration) + ' seconds')
    print('Total time between frame received and prediction: ' + str(stopwatchFrameProcessing.duration) + ' seconds')
    print('Total time for model to make a prediction: ' + str(stopwatchPrediction.duration) + ' seconds')
    print('Model Prediction: '+ str(test) + '\n')
    stopwatchFrameProcessing.reset()
    stopwatchPrediction.reset()
    stopwatchLoop.reset()
    if cv2.waitKey(1) & 0xFF == ord('l'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows