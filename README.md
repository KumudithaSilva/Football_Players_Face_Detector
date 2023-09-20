#  Football Player Image Classification ⚽🥅
Welcome to the Football Player Image Classification project! This project embarks on an exciting journey to classify football players from images. The aim is to provide users with a platform where images of football players can be uploaded, and the classification model will predict the correct player among four predefined classes.
<br><br>


![Sport_2](https://github.com/KumudithaSilva/Football_Players_Face_Detector/assets/131386682/74ca58cf-5448-4940-8aac-78280f20165d)

## Project Overview 📊
The primary objective of this project revolves around the construction of a classification model for football players to achieve accurate player predictions. To accomplish this task, various techniques were employed, including the curvelet transform and wavelet transform on images to extract features from cropped images, followed by vertical stacking. Additionally, a user-centric website will be created, and cloud platforms will empower users to access and utilize the developed model.

## Project Architecture 🏗️
This project follows these key steps:
- **Data Collection 📂:** The dataset is obtained from various sources, including web scraping using tools like "Fatkun Batch Download" for efficient image collection.
- **Data Preprocessing 🛠️:** Essential data preprocessing steps are performed, including resizing, grayscale conversion, color space conversion, rotation, and cropping to reduce noise and extract relevant information from the images in the dataset.
- **Data Cleaning 🧹:** To ensure data quality, Haar Cascade and manual verification are employed to detect and discard obstructed images, enhancing the cleanliness of the dataset.
- **Image Cropping ✂️:** Haar Cascade is used again to crop images, eliminating obstructed portions. This cleaned dataset is crucial for model training.
- **Feature Engineering 📷:** Leveraging OpenCV and techniques like curvelet and wavelet transforms, features are extracted from both the raw and wavelet-transformed images. These features are then vertically stacked for model training.
- **Machine Learning Model ⚙️:** A machine learning model for football player classification is built, utilizing Python's pandas and scikit-learn libraries. The model is also hyper-tuned to achieve optimal performance. Instead of deep learning, a traditional machine learning approach is adopted for training the classifier in this project.
- **Model Persistence 📦:** The trained model is exported to a pickle file for future use.
- **Flask Server ⚡:** A Python Flask server is developed to consume the pickle file of the trained model. This server exposes HTTP endpoints to handle prediction requests.
- **AWS Integration ☁️:** The Flask server and the trained model are deployed on AWS, leveraging its cloud capabilities for scalability and accessibility.
- **Web Application 🌐:** A user-friendly website is created using HTML, CSS, and JavaScript. This website communicates with the Flask server hosted on AWS to provide users with football player predictions.

## Tools and Technology 🛠️
The tools and technologies involved in this project include:
-	🐍 Python: Selected for its versatility in data processing, model building, and server development.
-	🐼 pandas: A robust library for efficient data manipulation and cleaning tasks.
-	🖼️ Fatkun Batch Download: An extension for efficient image collection.
-	📸 OpenCV: A powerful library for image processing, assisting in the extraction of valuable features.
-	🌌 PyWavelet: Used for wavelet transform, enabling effective feature extraction from images and enhancing the model's ability to capture intricate patterns.
-	🧠 scikit-learn: A widely-utilized machine learning library that offers an array of predictive modeling algorithms.
-	📊 Seaborn: Empowers the project with potent data visualization capabilities, facilitating insightful data exploration.
-	⚡ Python Flask: A micro web framework employed to establish the server, facilitating seamless model deployment.
-	🌐 HTML, CSS, JavaScript: Key front-end technologies seamlessly integrated to create interactive user interfaces.
-	☁️ AWS: Leveraged to host both the Flask server and trained model, ensuring scalability and user accessibility.
