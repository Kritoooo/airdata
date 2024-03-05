import pandas as pd
from darts import TimeSeries
from darts.dataprocessing.transformers import Scaler
from darts.models import TransformerModel
import torch
from matplotlib import pyplot as plt

from 数据分析.cityDict import get_city_list

# torch.load()
city_list = get_city_list()
Scalerlist = []
serieslist = []
vallist = []
pos = 0

for city in city_list:
    df = pd.read_csv("../airdata/outputdata/"+city+'.csv').loc[:,['date', 'OT']]
    # print(df)
    if df.shape[0] < 900:
        continue
    pos = pos + 1
    series = TimeSeries.from_dataframe(df = df, time_col="date", fill_missing_dates=False, freq="D")
    series = series[-1200:]
    scaler_tmp = Scaler()
    series_scaled = scaler_tmp.fit_transform(series)
    Scalerlist.append(scaler_tmp)
    train_data, val_data = series_scaled[:-200], series_scaled[-200:]
    serieslist.append(train_data)
    # print(train_data)
    vallist.append(val_data)

model = TransformerModel(input_chunk_length=60, output_chunk_length=30, n_epochs=5, dropout=0.1, save_checkpoints = True)
model.fit(series = serieslist[0], verbose=True)
# pred = model.predict(n=200, series = serieslist[0])
# pred = Scalerlist[0].inverse_transform(pred)
# true = Scalerlist[0].inverse_transform(vallist[0])
# true.plot(label='actual')
# pred.plot(label='forecast')
# pred
# plt.show()