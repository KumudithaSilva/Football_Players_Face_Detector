from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_images():
    images = request.form['images']

    response = jsonify(util.classify_image(images))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    

if __name__ == "__main__":
    print("Staring Python Flask Server for Image Classification")
    util.load_saved_artifacts()
    app.run()