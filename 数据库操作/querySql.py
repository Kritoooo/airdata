import pandas as pd

from 数据库操作.connnectMysql import *
def query(city, start_day, end_day, type):
    sql = query_sql.format(type,city,start_day, end_day)
    try:
        df = get_df(sql)
        return df
    except:
        print("查询失败")

def query_all(city, start_day, end_day):
    sql = query_all_sql.format(city, start_day, end_day)
    print(sql)
    try:
        return get_results(sql)
    except:
        print("查询失败")