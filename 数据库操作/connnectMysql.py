import pandas as pd
import pymysql

con = pymysql.connect(host='localhost', user= 'root', password='123456', database='airdata', port=3306)
cursor = con.cursor()

insert_sql = "insert into `{}` values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
query_sql = "select 日期,`{}` from {} where 日期 >= \'{}\' and 日期 <= \'{}\'"
query_all_sql = "select * from {} where 日期 >= \'{}\' and 日期 <= \'{}\' order by `{}` {}"
query_last_sql = "select * from {} order by 日期 desc limit {}"
def get_results(sql):
    cursor.execute(sql)
    results = cursor.fetchall()
    return results

def get_df(sql):
    results = get_results(sql)
    cols_info = cursor.description
    cols = [col[0] for col in cols_info]
    df = pd.DataFrame(results, columns=cols)
    return df

# 将数据库查询结果转化为dataframe格式
def to_df(results):
    cols_info = cursor.description
    cols = [col[0] for col in cols_info]
    df = pd.DataFrame(results, columns=cols)
    return df