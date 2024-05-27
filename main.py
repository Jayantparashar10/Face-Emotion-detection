import cv2 as cv
import numpy as np
import os
import time
import tensorflow as tf
from tensorflow import keras
from keras.models import load_model

# Camera capture
cap = cv.VideoCapture(0)  # 0 for default camera
if not cap.isOpened():
    print("Failed to open camera")
    exit()

ret, frame = cap.read()
if not ret:
    print("Failed to capture frame from camera")
    cap.release()
    cv.destroyAllWindows()
    exit()

# Display the captured frame
cv.imshow("Frame", frame)
cv.waitKey(0)

# Release the capture
cap.release()
cv.destroyAllWindows()
