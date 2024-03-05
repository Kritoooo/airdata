from io import StringIO

import pandas as pd
import requests

def get_pred(in_path, target_folder):
    print(in_path, target_folder)
    resp = requests.post("http://127.0.0.1:5000/predict",
                         files={"file": open(in_path,'rb')})
    df = pd.read_csv(StringIO(resp.content.decode()))
    df.to_csv(target_folder + '\\ans.csv')
    print(resp.content)

# get_pred("E:\pythonProject\暑期实训\\airdata\outputdata\\akesu.csv", ".\\test1")
