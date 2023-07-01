import pandas as pd
import numpy as np
# 定义污染物浓度分级标准表
bp_table = {
    'PM2.5': [0, 35, 75, 115, 150, 250, 350, 500],
    'PM10': [0, 50, 150, 250, 350, 420, 500, 600],
    'So2': [0, 50, 150, 475, 800, 1600, 2100, 2620],
    'No2': [0, 40, 80, 180, 280, 565, 750, 940],
    'Co': [0, 2, 4, 14, 24, 36, 48, 60],
    'O3': [0, 100, 160, 215, 265, 800]
}

# 定义空气质量分指数表
iaqi_table = [0, 50, 100, 150, 200, 300, 400, 500]


# 定义计算AQI的函数
def calculate_aqi(pollutant_concentration : float, pollutant_name: str) -> float:
    # 检查输入参数是否有效
    if pollutant_name not in bp_table:
        print(f'无效的污染物名称：{pollutant_name}')
        return None
    if pollutant_concentration < bp_table[pollutant_name][0]:
        print(f'无效的污染物浓度：{pollutant_concentration}')
        return None

    # 找到与测量浓度相邻的两个分级标准值
    bp_h = None
    bp_l = None
    for i in range(len(bp_table[pollutant_name]) - 1):
        if bp_table[pollutant_name][i] <= pollutant_concentration < bp_table[pollutant_name][i + 1]:
            bp_h = bp_table[pollutant_name][i + 1]
            bp_l = bp_table[pollutant_name][i]
            break

    # 找到对应的空气质量分指数值
    iaqi_h = iaqi_table[i + 1]
    iaqi_l = iaqi_table[i]

    # 根据公式计算AQI
    aqi = (iaqi_h - iaqi_l) / (bp_h - bp_l) * (pollutant_concentration - bp_l) + iaqi_l

    # 返回AQI值，保留两位小数
    return round(aqi, 2)

def get_level(aqi, type):
    redic = {'num':[1,2,3,4,5,6],'str':['优','良','轻度污染', '中度污染', '重度污染', '严重污染']}
    if aqi <= 50:
        return redic[type][0]
    elif aqi <= 100:
        return redic[type][1]
    elif aqi <= 150:
        return redic[type][2]
    elif aqi <= 200:
        return redic[type][3]
    elif aqi <= 300:
        return redic[type][4]
    else:
        return redic[type][5]