from datetime import datetime
from util.db_util.db_read import get_data



class course:
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
    def get_dataframe():
        return get_dataframe(course)