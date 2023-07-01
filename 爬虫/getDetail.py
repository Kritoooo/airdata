from bs4 import BeautifulSoup
import requests
import csv
with open("city_detail_url.txt", 'r') as f:
    cur = 0
    url_list = f.readlines()
    url_list = url_list[8035:]
    last_name = ""
    for url in url_list:
        cur = cur + 1
        print(cur)
        url = url[:-1]
        cnt = 0
        city_name = ""
        for i in range(len(url)):
            if url[i] == '-':
                break
            if cnt == 4:
                city_name = city_name + url[i]
            if url[i] == '/':
                cnt = cnt + 1
        # print(city_name)
        print(url)
        headers = {
            "headers" : "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14"
        }
        html = requests.get(url, headers = headers)
        print(1)
        html.encoding = 'GBK'
        soup = BeautifulSoup(html.text, 'lxml')
        date = soup.select("#content > div.api_month_list > table > tr > td")
        file_path = "E:\pythonProject\暑期实训\\airdata\\" + city_name + ".csv"
        with open(file_path, "a", encoding="utf-8", newline="") as f:
            cnt1 = 0
            csv_writer = csv.writer(f)
            list = []
            for item in date:
                content = item.text.split(None)
                list.append(content[0])
                # print(content)
                if len(list) == 10:
                    cnt1 = cnt1 + 1
                    # print(cnt1)
                    if cnt1 == 1:
                        if city_name == last_name:
                            list = []
                            continue
                    csv_writer.writerow(list)
                    list = []
            f.close()
        last_name = city_name
