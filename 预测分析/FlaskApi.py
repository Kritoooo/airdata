import io
import json

import matplotlib.pyplot as plt
import pandas as pd
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request, send_file
from torchvision import models
import model_predict

app = Flask(__name__)
def get_predict_result():
    print(1)
    df = pd.read_csv('in.csv').loc[:, ['date', 'OT']]
    series = model_predict.TimeSeries.from_dataframe(df=df, time_col="date", fill_missing_dates=False, freq="D")
    scaler_tmp = model_predict.Scaler()
    series = scaler_tmp.fit_transform(series)
    pred = model_predict.model.predict(n=30, series = series)
    pred = scaler_tmp.inverse_transform(pred)
    pred.plot(label='forecast')
    plt.savefig('plot')
    pred.to_csv('pred.csv')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        file.save('in.csv')
        get_predict_result()
    return send_file('pred.csv')


if __name__ == '__main__':
    app.run()
