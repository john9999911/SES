import pandas as pd

from util.db_util.db_connector import get_con

con = None


def get_dataframe(cls):
    global con
    if con is None:
        con = get_con()
    sql = "select * from " + "t_stat_{}".format(cls.__name__)
    df = pd.read_sql(sql, con)
    return df
