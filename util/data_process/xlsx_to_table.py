# -*- coding: utf-8 -*-

import pandas as pd
from util.db_util.db_connector import get_con, execute_sql


# 读取xlsx文件，创建数据库表，文件中只有表信息没有数据，有多个表
# 第一列为表名，第二列为表描述，合并了单元格，第三列为字段名，第四列为字段类型，可能为空，为空时使用Integer，第五列为字段描述，可能为空
# 第二行开始为数据
def convert(path: str):
    sqls = []
    # 读取xlsx文件
    df = pd.read_excel(path, sheet_name=0)
    for table_name, table_desc in zip(df['表名'], df['表描述']):
        if pd.isna(table_name):
            break
        # 创建数据库表
        create_table_sql = 'create table if not exists ' + table_name + ' ('
        # 读取表字段信息
        table_df = df[df['表名'] == table_name]
        for field_name, field_type, field_desc in zip(table_df['字段'], table_df['类型'], table_df['描述']):
            if pd.isna(field_type):
                field_type = 'Integer'
            if pd.isna(field_desc):
                field_desc = ''
            create_table_sql += field_name + ' ' + field_type + ' comment \'' + field_desc + '\','
        create_table_sql = create_table_sql[:-1] + ') comment \'' + table_desc + '\';'
        print(create_table_sql)
        sqls.append(create_table_sql)
    # 执行sql语句
    execute_sql(get_con(), sqls)


if __name__ == '__main__':
    convert('../../data/数据包字段说明.xlsx')