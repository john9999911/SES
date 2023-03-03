# -*- coding: utf-8 -*-

import pandas as pd
from util.db_util.db_connector import get_con


def convert(paths: list):
    for path in paths:
        table_name = path.split('\\')[-1].split('.')[0] if '\\' in path else path.split('/')[-1].split('.')[0]
        # 读取xlsx文件
        df = pd.read_excel(path)
        # 将数据写入数据库
        df.to_sql(table_name, get_con(), if_exists='append', index=False)


if __name__ == '__main__':
    convert(['../../data/地大数据/公网数据/t_stat_activity_log.xls'])
