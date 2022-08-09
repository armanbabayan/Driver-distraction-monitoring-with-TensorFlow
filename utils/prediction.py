import tensorflow as tf
import cv2
import numpy as np
from utils.decorators import timer

def resize_image(filepath, img_size= None):

    """
    Function takes file path as an input. Returns resized image.

    :param filepath: image file path
    :param img_size: target size of the image
    :return: resized image
    """
    if img_size is None:
        img_size = 256
    
    img_array = cv2.imread(filepath)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)
    new_array = cv2.resize(img_array, (img_size, img_size))

    return new_array.reshape(img_size, img_size, 3)

@timer
def make_prediction(image_path, model_path, class_list):
    """

    :param image_path: The image path to predict
    :param model_path: Model path
    :param class_list: List of class names of the current model
    :return: tuple. First element is predicted class name,
             second element is confidence score of predicted class
    """

    model = tf.keras.models.load_model(model_path)
    image = resize_image(image_path)
    image_batch = np.expand_dims(image, 0)
    prediction = model.predict(image_batch)
    confidence = round(100 * (np.max(prediction[0])), 2)
    return class_list[np.argmax(prediction[0])], confidence
