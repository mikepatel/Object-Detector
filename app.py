"""
Michael Patel
March 2020

Project description:
    Build a basic object detector that uses PC webcam

File description:
    For running object detector through webcam

"""
################################################################################
# Imports
import os
import numpy as np
import cv2
import tensorflow as tf


################################################################################
# Main
if __name__ == "__main__":
    # open webcam and capture video
    capture = cv2.VideoCapture(0)  # 0 = first camera

    while True:
        # capture frame by frame
        ret, frame = capture.read()

        # display resulting frame
        cv2.imshow("", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # release capture
    capture.release()
    cv2.destroyAllWindows()

    # use pretrained model

