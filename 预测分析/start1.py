import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from torchmetrics import MeanAbsoluteError, MetricCollection
import pandas as pd
import numpy as np
import torch
import matplotlib.pyplot as plt

from darts import TimeSeries
from darts.utils.timeseries_generation import gaussian_timeseries, linear_timeseries, sine_timeseries
from darts.models import RNNModel, TCNModel, TransformerModel, NBEATSModel, LinearRegressionModel
from darts.metrics import mape, smape, mse
from darts.dataprocessing.transformers import Scaler
from darts.utils.timeseries_generation import datetime_attribute_timeseries
from darts.datasets import AirPassengersDataset, MonthlyMilkDataset

torch.manual_seed(1);
np.random.seed(1)  # for reproducibility

from 数据分析.cityDict import get_city_list
from 数据库操作.connnectMysql import get_df

sql = "select * from {}"
city_list = get_city_list()
print(city_list)
Scalerlist = []
serieslist = []
vallist = []
pos = 0
for city in city_list:
    df = get_df(sql.format(city)).drop(columns=["质量等级", "当天AQI排名", "当天AQI排名","PM2.5","PM10","So2","No2","Co","O3"])
    if df.shape[0] < 900:
        continue
    pos = pos + 1
    print(pos)
    df.rename(columns={'日期': 'date', 'AQI指数' : "#Passengers"}, inplace=True)
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')
    df['date'] = df['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
    df['#Passengers'] = df['#Passengers'].astype(float)
    series = TimeSeries.from_dataframe(df = df, time_col="date", fill_missing_dates=False, freq="D")
    series = series[-900:]
    serieslist.append(series)
    scaler_tmp = Scaler()
    series_scaled = scaler_tmp.fit_transform(series)
    Scalerlist.append(scaler_tmp)
    train_data, val_data = series_scaled[:-36], series_scaled[-36:]
    serieslist.append(train_data)
    vallist.append(val_data)

print(vallist)

print(1)
model = TransformerModel(input_chunk_length=60, output_chunk_length=30, n_epochs=40, dropout=0.1, save_checkpoints = True)
model.fit(train_data, verbose=True, val_series = vallis)
pred = model.predict(n=36, series=serieslist[0][:-36])

vallist[0].plot(label='actual')
pred.plot(label='forecast')
plt.show()