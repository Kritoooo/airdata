import csv
import datetime
import chardet
import numpy as np
from decimal import *

from 数据分析.cityDict import get_city_list
from 文件操作.encode_judge import get_encode_info
from connnectMysql import *

file_path = "..\\alldata\{}.csv"
city_list = get_city_list()

def trans_type(item):
    # item[0] = datetime.datetime.strptime(item[0], '%Y/%m/%d').strftime("%Y-%m-%d")
    for i in range(2,10):
        if i == 8:
            item[i] = float(item[i])
        else:
            item[i] = int(item[i])
    return item

for city in city_list:
    if city == '北京':
        continue
    try:
        f = file_path.format(city)
        print(f)
        encode_info = get_encode_info(f)
        print(encode_info)
        data = csv.reader(open(file_path.format(city), encoding=encode_info))
        print("导入数据中--{}--".format(city))
        for item in data:
            if item[0] == "日期":
                continue
            item = trans_type(item)
            sql = insert_sql.format(city)
            try:
                cursor.execute(sql,tuple(item))
                con.commit()
            except:
                print("重复数据已跳过")
    except:
        continue
