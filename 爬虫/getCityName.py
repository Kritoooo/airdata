from bs4 import BeautifulSoup
import requests

url = "http://www.tianqihoubao.com/aqi/"
headers = {
    "headers" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36"
}
html = requests.get(url, headers = headers)
html.encoding = 'GBK'
soup = BeautifulSoup(html.text, 'lxml')
# print(soup)
city_name = soup.select("#content > div.citychk > dl > dd > a")
with open('city_name.txt', 'w') as f:
    for item in city_name:
        print(item.text)
        f.write(item.text + ',')