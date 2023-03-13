from datetime import datetime

from util.db_util.db_read import get_data


# id
# insert_time
# create_time
# last_modify_time
# personid
# name
# chapter_count
# course_number
# is_deleted
# group_name
# courseid
# fid
# 这是课程表 t_stat_course

class course:
    # 带有time的参数，需要在参数后面加上datetime
    # 不带有time的参数，加：str
    # 例如：def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, fid: str):
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, name: str, chapter_count: str, course_number: str, is_deleted: str, group_name: str, courseid: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.name = name
        self.chapter_count = chapter_count
        self.course_number = course_number
        self.is_deleted = is_deleted
        self.group_name = group_name
        self.courseid = courseid
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(course)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)