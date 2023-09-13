from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET', 'POST'])
def hello():
    return "Hi"

if __name__ == "__main__":
    app.run()