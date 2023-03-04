# -*- coding: utf-8 -*-

import pandas as pd
from util.db_util.db_connector import get_con, execute_sql


# 读取xlsx文件，创建数据库表，文件中只有表信息没有数据，有多个表
# 第一列为表名，第二列为表描述，合并了单元格，第三列为字段名，第四列为字段类型，可能为空，为空时使用Integer，第五列为字段描述，可能为空
# 第二行开始为数据
def convert(path: str):
    sqls = []
    sql = ""
    # 读取xlsx文件
    df = pd.read_excel(path, sheet_name=0)
    table_name = ""
    table_desc = ""
    realKey = ""
    for index, row in df.iterrows():
        # row[0] 不为nan时，说明是表信息
        if not pd.isna(row[0]):
            if sql != "":
                sql += f"    PRIMARY KEY (id))"
                sqls.append(sql)
                print(sql)
                sql = ""
            table_name = row[0]
            table_desc = row[1]
            sql = f"CREATE TABLE {table_name} ("
        field_name = row[2]
        field_type = row[3]
        field_desc = row[4]
        # field_name 已经存在时，跳过
        if field_name in sql.split(" "):
            continue
        if pd.isna(field_type):
            field_type = "int(100)"
        # # 如果类型没有写长度，添加长度
        # if field_type.strip()[-1] != ')' and "datetime" not in field_type:
        #     field_type += "(100)"
        # if field_type == "datetime":
        #     field_type += "(6)"
        if pd.isna(field_desc):
            field_desc = ""
        sql += f"    {field_name} {field_type} ,"

    # 执行sql语句
    execute_sql(get_con(), sqls)
    # print(sqls)


if __name__ == '__main__':
    convert('../../data/数据包字段说明.xlsx')
