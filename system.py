#!/usr/bin/env python

from time import sleep           # Allows us to call the sleep function to slow down our loop
import RPi.GPIO as GPIO           # Allows us to call our GPIO pins and names it just GPIO
import start

import numpy as np
import pandas as pd
import random
import os

import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import sys
import time
import tensorflow.keras as keras
import tensorflow as tf
import re

from PIL import Image
from keras.layers import Input, Conv2D, Dense, Flatten, MaxPooling2D, Input, GlobalAveragePooling2D
from keras.layers.experimental.preprocessing import Normalization
from keras.models import Model, Sequential
from keras.preprocessing import image
from keras.utils import to_categorical
from keras.layers import Lambda
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import keras.applications.mobilenet_v2 as mobilenetv2

import numpy as np
from keras.preprocessing import image
from keras.models import load_model

import serial
ser = serial.Serial('/dev/ttyACM1',9600)
ser.reset_input_buffer()
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)           # Set's GPIO pins to BCM GPIO numbering
INPUT_PIN = 18    # Sets our input pin, in this example I'm connecting our button to pin 4. Pin 0 is the SDA pin so I avoid using it for sensors/buttons
GPIO.setup(INPUT_PIN, GPIO.IN)           # Set our input pin to be an input
# OUTPUT_PIN_REC = 15
# OUTPUT_PIN_TRASH = 18
# GPIO.setup(OUTPUT_PIN_REC, GPIO.OUT)
# GPIO.setup(OUTPUT_PIN_TRASH, GPIO.OUT)

def recyclable(pred):
    rev_dict = {0: 'battery', 1: 'biological', 2: 'brown-glass', 3: 'cardboard', 4: 'clothes', 5: 'green-glass', 6: 'metal', 7: 'paper', 8: 'plastic', 9: 'trash', 10: 'white-glass'}
    if pred[1] in ['brown-glass', 'cardboard', 'green-glass', 'metal', 'paper', 'plastic', 'white-glass']:
        return True
    return False

# while True:
#     if ser.in_waiting > 0:
#         line = ser.readline().decode('utf-8').rstrip()
#         print(line)

# Start a loop that never ends
while True: 
    print(GPIO.input(INPUT_PIN))
    if (GPIO.input(INPUT_PIN) == 1): # Physically read the pin now
        print('take PIC now please')
        os.system("rpicam-jpeg -o test.jpg")
        print(pred:=start.detect("test.jpg"))
        if recyclable(pred):
            ser.write("recycle\n".encode('ascii'))
            print("wrote!")
        else:
            ser.write("trash\n".encode('ascii'))
        sleep(20)
    else:
        print('not yet, still low')

    sleep(1)         # Sleep for a full second before restarting our loop