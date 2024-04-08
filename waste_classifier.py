import tensorflow as tf
import tflite_runtime.interpreter as tflite
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import argparse
import cv2
from picamera2 import MappedArray, Picamera2, Preview

model = load_model("classifyWaste.h5")
output_class = ["batteries", "clothes", "e-waste", "glass", "light blubs", "metal", "organic", "paper", "plastic"]

def waste_prediction(new_image):
    test_image = image.load_img(new_image, target_size = (224,224))
    plt.axis("off")
    plt.imshow(test_image)
    plt.show()

    test_image = image.img_to_array(test_image) / 255
    test_image = np.expand_dims(test_image, axis=0)

    predicted_array = model.predict(test_image)
    predicted_value = output_class[np.argmax(predicted_array)]
    predicted_accuracy = round(np.max(predicted_array) * 100, 2)

    print("Your waste material is ", predicted_value, " with ", predicted_accuracy, " % accuracy")
    return predicted_value

def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--model', help='Path of the detection model.', required=True)
    # parser.add_argument('--label', help='Path of the labels file.')
    # parser.add_argument('--output', help='File path of the output image.')
    # args = parser.parse_args()

    # if (args.output):
    #     output_file = args.output
    # else:
    #     output_file = 'out.jpg'

    # if (args.label):
    #     label_file = args.label
    # else:
    #     label_file = None
    waste_prediction("test.png")

if __name__ == '__main__':
    main()
