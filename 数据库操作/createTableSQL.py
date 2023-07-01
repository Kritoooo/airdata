# 批量创建表
import pymysql
from 数据分析.cityDict import get_city_list

con = pymysql.connect(host='localhost', user= 'root', password='123456', database='airdata', port=3306)

cur = con.cursor()

createSql = """
create table airdata.`{}`
(
    日期        date    not null primary key,
    质量等级    char(5) null,
    AQI指数     int     null,
    当天AQI排名 int     null,
    `PM2.5`     int     null,
    PM10        int     null,
    So2         int     null,
    No2         int     null,
    Co          float(5,3)     null,
    O3          int     null
);
"""

city_list = get_city_list()
try:
    for item in city_list:
        sql = createSql.format(item)
        cur.execute(sql)
        print("创建{}表成功".format(item))
except Exception as e:
    print(e)
    print("创建失败")
finally:
    cur.close()
    con.close()
