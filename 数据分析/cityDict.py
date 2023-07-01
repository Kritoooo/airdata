from xpinyin import Pinyin
p = Pinyin()
dict = {}
dict1 = {}
with open('..\\爬虫\\city_name.txt','r') as f:
    city_name = f.readline().split(' ,')
    for item in city_name:
        ans = p.get_pinyin(item,splitter="")
        if item == "重庆":
           ans = "chongqing"
        dict[ans] = item
        dict1[item] = ans

def city_to_pinyin(city):
    return dict[city]

def get_city_list():
    return dict.keys()

def pinyin_to_city(city):
    return dict1[city]