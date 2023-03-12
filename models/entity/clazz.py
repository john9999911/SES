from datetime import datetime

from util.db_util.db_read import get_data


# id
# insert_time
# create_time
# last_modify_time
# personid
# name
# clazz_number
# student_count
# courseid
# semester
# is_deleted
# clazzid
# fid

class clazz:
    # 带有time的参数，需要在参数后面加上datetime
    # 不带有time的参数，加：str
    # 例如：def __init__(self, id: str, insert_time: datetime, fid: str):
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, name: str, clazz_number: str, student_count: str, courseid: str, semester: str, is_deleted: str, clazzid: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.name = name
        self.clazz_number = clazz_number
        self.student_count = student_count
        self.courseid = courseid
        self.semester = semester
        self.is_deleted = is_deleted
        self.clazzid = clazzid
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(clazz)