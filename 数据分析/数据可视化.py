import pandas as pd
import matplotlib.pyplot as plt
from 数据分析.预处理 import *
from 数据分析 import cityDict
from 数据库操作.querySql import *
# 设置绘图风格
plt. style.use("ggplot")
# 设置中文编码和符号的正常显示
plt.rcParams["font.sans-serif"] = "KaiTi"
plt.rcParams["axes.unicode_minus"] = False

pollutants = ['PM2.5', 'PM10', 'So2', 'No2', 'Co', 'O3']
def get_data(city, type, start, end):
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    period = (end - start).days
    end = end.strftime("%Y-%m-%d")
    start = start.strftime("%Y-%m-%d")
    city = cityDict.pinyin_to_city(city)
    print(city, type, start, end)
    sub_data = query(city, start, end, type)
    return sub_data, period, city

def get_all_data(city, start, end):
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)
    period = (end - start).days
    end = end.strftime("%Y-%m-%d")
    start = start.strftime("%Y-%m-%d")
    city = cityDict.pinyin_to_city(city)
    print(city, start, end)
    sub_data = query_all(city, start, end)
    return sub_data, period, city

def drawplot(sub_data, city, type, day):
    city = cityDict.city_to_pinyin(city)
    # 设置图框的大小
    fig = plt.figure(figsize=(10, 6))
    # 绘图
    plt.plot(sub_data['日期'],  # x轴数据
             sub_data[type],  # y轴数据
             linestyle='-',  # 折线类型
             linewidth=2,  # 折线宽度
             color='steelblue',  # 折线颜色
             marker='o',  # 点的形状
             markersize=6,  # 点的大小
             markeredgecolor='black',  # 点的边框色
             markerfacecolor='brown')  # 点的填充色
    suf_str = ""

    if type == "AQI指数" or type == "当天AQI排名":
        suf_str = "趋势图"
    else:
        suf_str = "含量趋势图"

    photo_title = city + str(day) + "日" + type + suf_str
    y_name = type
    if y_name == "Co ":
        y_name = y_name + "mg/m3"
    elif y_name != "AQI指数" and y_name != "当天AQI排名":
        y_name = y_name + "ug/m3"
    else:
        y_name = type
    # 添加标题和坐标轴标图
    plt.title(photo_title)
    plt.xlabel('日期')
    plt.ylabel(y_name)
    # 剔除图框上边界和右边界的刻度
    plt.tick_params(top='off', right='off')

    # 为了避免x轴日期刻度标签的重叠，设置x轴刻度自动展现，并且45度倾斜
    fig.autofmt_xdate(rotation=45)
    plt.savefig("plot.jpg")
    plt.close()


def draw_plot(city, type, start, end):
    sub_data, period, city = get_data(city, type, start, end)
    drawplot(sub_data,city,type,period)

def drawpie(sub_data, city, type, day):
    city = cityDict.city_to_pinyin(city)
    colors = ['green', 'yellow', 'orange', 'red', 'purple', 'darkred']
    fig = plt.figure(figsize=(10, 6))
    if type == "AQI指数":
        type = "空气"
    photo_title = city + str(day) + "日" + type + "质量等级分布情况"
    plt.pie(sub_data, labels=sub_data.index, colors=colors)
    plt.title(photo_title)
    plt.savefig("pie.jpg")
    plt.close()

def draw_pie(city, type, start, end):
    if type == "AQI指数":
        sub_data, period, city = get_data(city, "质量等级", start, end)
    else:
        sub_data, period, city = get_data(city, type, start, end)
        sub_data[type] = sub_data[type].astype(float)
        sub_data['质量等级'] = sub_data[type].apply(calculate_aqi, args=(type, ))
        sub_data['质量等级'] = sub_data['质量等级'].apply(get_level, args=("str",))
    # print(sub_data)
    sub_data = sub_data['质量等级'].value_counts()
    drawpie(sub_data, city, type, period)

def drawhist(sub_data, city, period):
    all_sum = 0
    x_data = {}
    city = cityDict.city_to_pinyin(city)
    fig = plt.figure(figsize=(10, 6))
    for pollutant in pollutants:
        ans = sub_data[pollutant].sum() / sub_data.shape[0]
        all_sum = all_sum + ans
        x_data[pollutant] = ans
    for pollutant in pollutants:
        plt.bar(pollutant,x_data[pollutant])
    plt.title(city+"市"+"各污染物对空气质量的影响")
    plt.xlabel("污染物名称")
    plt.ylabel("平均AQI")
    # plt.show()
    plt.savefig("hist.jpg")
    plt.close()

def draw_hist(city,start,end):
    sub_data, period, city = get_all_data(city, start, end)
    sub_data = to_df(sub_data)
    # print(sub_data)
    for pollutant in pollutants:
        sub_data[pollutant] = sub_data[pollutant].astype(float)
        sub_data[pollutant] = sub_data[pollutant].apply(calculate_aqi, args = (pollutant,))
    drawhist(sub_data, city, period)

city = "北京"
start = "2014-01-01"
end = "2015-01-01"
type = "AQI指数"

# draw_pie(city, type, start, end)




