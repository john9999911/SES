import pandas as pd

from util.db_util.db_connector import get_con


# 参数：类指针
# 返回：类实例
def get_data(cls):
    con = get_con()
    cursor = con.cursor()
    sql = "select * from " + "t_stat_{}".format(cls.__name__)
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    con.close()
    # 将每行数据转换为类实例
    return [cls(*row) for row in data]


def get_dataframe(cls):
    con = get_con()
    sql = "select * from " + "t_stat_{}".format(cls.__name__)
    df = pd.read_sql(sql, con)
    con.close()
    return df
