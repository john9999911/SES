# id
# insert_time
# create_time
# last_modify_time
# dtype
# personid
# courseid
# clazzid
# start_time
# end_time
# ip
# activity_id
# attend_count
# send_to_student
# fid
# 这是课堂活动发布表 t_stat_widget_log

from datetime import datetime

from util.db_util.db_read import get_data


class widget_log:
    # 带有time的参数，需要在参数后面加上datetime
    # 不带有time的参数，加：str
    # 例如：def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, fid: str):
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, dtype: str, personid: str, courseid: str, clazzid: str, start_time: datetime, end_time: datetime, ip: str, activity_id: str, attend_count: str, send_to_student: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.dtype = dtype
        self.personid = personid
        self.courseid = courseid
        self.clazzid = clazzid
        self.start_time = start_time
        self.end_time = end_time
        self.ip = ip
        self.activity_id = activity_id
        self.attend_count = attend_count
        self.send_to_student = send_to_student
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(widget_log)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)