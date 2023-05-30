from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from plant.utils import decodeImage
from plant.pipeline.predict import Plant
import base64

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = Plant(self.filename)


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/train", methods=['GET','POST'])
@cross_origin()
def trainRoute():
    os.system("python main.py")
    return "Training done successfully!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    with open(clApp.filename, "wb") as img_file:
        img_file.write(base64.b64decode(image))
    result = clApp.classifier.prediction()
    return jsonify({"result": result})


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=8080)
