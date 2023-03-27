import datetime

from util.db_util.db_read import get_data, get_dataframe


class exam_relation:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, score: str, start_time: datetime, end_time: datetime, specified_time: datetime, clazzid: str, isDeleted: str, exam_id: str, paper_library_id: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.score = score
        self.start_time = start_time
        self.end_time = end_time
        self.specified_time = specified_time
        self.clazzid = clazzid
        self.isDeleted = isDeleted
        self.exam_id = exam_id
        self.paper_library_id = paper_library_id
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(exam_relation)

    @staticmethod
    def get_dataframe():
        return get_dataframe(exam_relation)