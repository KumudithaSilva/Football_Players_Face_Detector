import numpy as np
import pywt
import cv2
import os
import base64
import json
import joblib
import pickle
from wavelet import w2d

# Get the absolute path of the server directory
artifacts_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to files
class_file_path = os.path.join(artifacts_directory, "artifacts", "class_dictionary.json")
model_file_path = os.path.join(artifacts_directory, "artifacts", "best_model.pkl")

# Variables to hold loaded data
__class_name_number = None
__class_number_name = None
__model = None

# Load artifacts files
def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __class_name_number
    global __class_number_name
    global __model

    # Read the JSON file
    with open(class_file_path, 'r') as file:
        __class_name_number = json.load(file)
        __class_number_name = {v: k for k, v in __class_name_number.items()}

    # Load the pickle file
    with open(model_file_path, 'rb') as file:
        __model = joblib.load(file)

    print("Successfully loaded the artifacts...")

# Get the based64 string file
def get_b64_test_image():
    with open("FootballPlayerImageClassifier/server/b64.txt", 'r') as file:
        return file.read()
    
# Decode the based64 string
def get_cv2_image_from_based64_string(b64str):
    encoded_data = b64str.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

# Get the cropped image
def get_cropped_image(image_path, image_based64):
    face_cascade = cv2.CascadeClassifier('FootballPlayerImageClassifier/server/opencv/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('FootballPlayerImageClassifier/server/opencv/haarcascade_eye.xml')

    if image_path:
        img = cv2.imread(image_path)
    else:
        img = get_cv2_image_from_based64_string(image_based64)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)

    cropped_faces = []
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes) >= 2:
            cropped_faces.append(roi_color)
    return cropped_faces

# Classify the image
def classify_image(image_based64, file_path=None):
    imgs = get_cropped_image(file_path, image_based64)

    results = []
    for img in imgs:
        scalled_row_image = cv2.resize(img, (32, 32))
        img_har = w2d(img, 'db1', 5)
        scalled_img_har = cv2.resize(img_har, (32, 32))
        comnined_img = np.vstack((scalled_row_image.reshape(32 * 32 * 3, 1), scalled_img_har.reshape(32 * 32, 1)))

        len_image_array = 32 * 32 * 3 + 32 * 32

        final = comnined_img.reshape(1, len_image_array).astype(float)

        results.append({
            'class' : class_name(__model.predict(final)[0]),
            'class_probability' : np.round(__model.predict_proba(final) * 100, decimals=2).tolist()[0],
            'class_dictionary' : __class_name_number
            })
        
    return results

# Class number to name converstion
def class_name(number):
    name = __class_number_name[number]
    return name


if __name__ == '__main__':
    load_saved_artifacts()
    print(classify_image(get_b64_test_image(), None))
    print(classify_image(None, "FootballPlayerImageClassifier/server/test_images/1.jpg"))
    print(classify_image(None, "FootballPlayerImageClassifier/server/test_images/2.jpg"))
    print(classify_image(None, "FootballPlayerImageClassifier/server/test_images/3.png"))
    print(classify_image(None, "FootballPlayerImageClassifier/server/test_images/4.jpg"))
