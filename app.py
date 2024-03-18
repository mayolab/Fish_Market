import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

model = pickle.load(open("fish-model.pkl", "rb"))


@app.route('/predict', methods=['POST'])

def predict():

    data = request.get_json()

    df = pd.DataFrame(data)

    prediction = model.predict(df)

    return jsonify({'species': prediction[0]})


if __name__ == '__main__':

    app.run(debug=True)

