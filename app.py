import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = pickle.load(open("fish-model.pkl", "rb"))

@app.route('/', methods=['GET'])

def home():
    return render_template('index.html'),200


@app.route('/predict', methods=['POST'])

def predict():

    if request.headers['Content-Type'] == 'application/json':
        weight = request.get_json()['weight']
        length1 = request.get_json()['length1']
        length2 = request.get_json()['length2']
        length3 = request.get_json()['length3']
        height = request.get_json()['height']
        width = request.get_json()['width']
    else:
        #question = request.form.get('input', '')

        weight = request.form.get('weight', '')
        length1 = request.form.get('length1', '')
        length2 = request.form.get('length2','')
        length3 = request.form.get('length3','')
        height = request.form.get('height','')
        width = request.form.get('width','')




    data = request.get_json()

    df = [[weight, length1, length2, length3, height, width]]

    prediction = model.predict(df)

    return jsonify({'species': prediction[0]})


if __name__ == '__main__':

    app.run(debug=True)
