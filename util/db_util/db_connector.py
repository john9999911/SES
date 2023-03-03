import os

import pymysql
import yaml


# 读yml配置
def read_yml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


# 连接数据库
def connect_db(db_config):
    return pymysql.connect(
        host=db_config['host'],
        port=db_config['port'],
        user=db_config['user'],
        password=db_config['password'],
        db=db_config['db'],
        charset=db_config['charset'],
    )


# 执行sql语句
def execute_sql(conn, sqls: list):
    cursor = conn.cursor()
    for sql in sqls:
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def get_con():
    # 读取配置
    db_config = read_yml('../db_util/config.yml')
    # 连接数据库
    conn = connect_db(db_config)
    return conn
