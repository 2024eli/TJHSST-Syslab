import tensorflow as tf
import tflite_runtime.interpreter as tflite
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import argparse
import cv2
from picamera2 import MappedArray, Picamera2, Preview
from real_time_with_labels import InferenceTensorFlow, DrawRectangles

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', help='Path of the detection model.', required=True)
    parser.add_argument('--label', help='Path of the labels file.')
    parser.add_argument('--output', help='File path of the output image.')
    args = parser.parse_args()

    if (args.output):
        output_file = args.output
    else:
        output_file = 'out.jpg'

    if (args.label):
        label_file = args.label
    else:
        label_file = None
    # waste_prediction("test.png")

if __name__ == '__main__':
    main()
