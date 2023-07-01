from bs4 import BeautifulSoup
import requests
from xpinyin import  Pinyin
city_name = []
with open("city_name.txt", "r", encoding='gbk') as f:  #打开文本
    data = f.read()   #读取文本
    city_name = data.split(' ,')
p = Pinyin()
with open("city_detail_url.txt", "w") as f:
    for city in city_name:
        for year in range(2013,2024):
            start = 1
            end = 13
            if year == 2013:
                start = 10
            if year == 2023:
                end = 6
            for month in range(start,end):
                if month < 10:
                    date = str(year) + "0" + str(month)
                else:
                    date = str(year) + str(month)
                city = p.get_pinyin(city, '')
                url = "http://www.tianqihoubao.com/aqi/" + city + "-" + date + ".html"
                print(url, file= f)
