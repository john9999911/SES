# id
# insert_time
# create_time
# last_modify_time
# personid
# courseid
# title
# isDeleted
# work_library_id
# fid
# 这是作业表 t_stat_work_library
from datetime import datetime

from util.db_util.db_read import get_data


class work_library:
    # 带有time的参数，需要在参数后面加上datetime
    # 不带有time的参数，加：str
    # 例如：def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, fid: str):
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, title: str, isDeleted: str, work_library_id: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.title = title
        self.isDeleted = isDeleted
        self.work_library_id = work_library_id
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(work_library)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)