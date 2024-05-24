
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

import argparse

import cv2
import numpy as np

import os

def params(size):
    max = int(size**0.5)
    possible_sizes = [(i, size//i) for i in range(1, max+1) if size % i == 0]
    width, height = min(possible_sizes, key=lambda x: abs(x[0] - size/x[0]))
    if width > height: width, height = height, width
    return width, height

def detect(i):
    # Increasing the image size didn't result in increasing the training accuracy
    arr_img = []
    arr_prob = []
    IMAGE_WIDTH = 224    
    IMAGE_HEIGHT = 224
    IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
    IMAGE_CHANNELS = 3

    normalSize = (640, 480)
    lowresSize = (320, 240)

    model = load_model('waste_classify_model.h5')

    img = image.load_img(i, target_size = IMAGE_SIZE)
    arr_img.append(img)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis = 0)
    preds = model.predict(img)
    # print(preds)
    rev_dict = {0: 'battery', 1: 'biological', 2: 'brown-glass', 3: 'cardboard', 4: 'clothes', 5: 'green-glass', 6: 'metal', 7: 'paper', 8: 'plastic', 9: 'trash', 10: 'white-glass'}

    for i, p in enumerate(preds):
        index=np.argmax(p)
        klass=rev_dict[index]    
        prob=p[index]
        arr_prob.append((prob, klass))
    return arr_prob[0]

# def main():
#     os.system("rpicam-jpeg -o test.jpg")
#     # print(detect("test.jpg"))

# if __name__ == '__main__':
#     main()