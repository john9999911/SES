# id
# insert_time
# create_time
# last_modify_time
# personid
# courseid
# clazzid
# type
# fid
# 这是其它活动流水  t_stat_log

from datetime import datetime

from util.db_util.db_read import get_data


class log:
    # 带有time的参数，需要在参数后面加上datetime
    # 不带有time的参数，加：str
    # 例如：def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, fid: str):
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, clazzid: str, type: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.clazzid = clazzid
        self.type = type
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(log)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)