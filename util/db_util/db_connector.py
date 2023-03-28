import os
from sqlalchemy import create_engine
import pymysql
import yaml


# 读yml配置
def read_yml(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.load(f, Loader=yaml.FullLoader)


# 执行sql语句
def execute_sql(conn, sqls: list):
    cursor = conn.cursor()
    for sql in sqls:
        cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()


def get_con():
    # 读取当前文件路径
    pre_path = os.path.abspath(__file__)
    path = os.path.join(os.path.dirname(pre_path), 'config.yml')
    print(path)
    # 读取配置
    db_config = read_yml(path)
    # 连接数据库

    engine = create_engine('mysql+pymysql://' + str(db_config['user']) + ':' + str(db_config['password']) + '@' + str(
        db_config['host']) + ':' + str(db_config['port']) + '/' + str(db_config['db']) + '?charset=' + str(
        db_config['charset']))
    conn = engine.connect()
    return conn
