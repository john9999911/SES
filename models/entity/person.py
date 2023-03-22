# id
# insert_time
# create_time
# last_modify_time
# personid
# user_name
# login_name
# role
# fid
#这是用户信息表 t_stat_person
from datetime import datetime

from util.db_util.db_read import get_data


class person:
    # 带有time的参数，需要在参数后面加上datetime
    # 不带有time的参数，加：str
    # 例如：def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, fid: str):
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, user_name: str, login_name: str, role: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.user_name = user_name
        self.login_name = login_name
        self.role = role
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(person)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)