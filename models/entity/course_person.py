from datetime import datetime

from util.db_util.db_read import get_data


# id
# insert_time
# create_time
# last_modify_time
# personid
# courseid
# clazzid
# isDeleted
# role
# fid
# 这是人课关系表 t_stat_course_person

class course_person:
    # 带有time的参数，需要在参数后面加上datetime
    # 不带有time的参数，加：str
    # 例如：def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, fid: str):
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, clazzid: str, isDeleted: str, role: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.clazzid = clazzid
        self.isDeleted = isDeleted
        self.role = role
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(course_person)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)