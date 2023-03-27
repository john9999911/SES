from datetime import datetime

from util.db_util.db_read import get_data, get_dataframe


class work_relation:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, score: str, clazzid: str, isDeleted: str, work_id: str, work_library_id: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.score = score
        self.clazzid = clazzid
        self.isDeleted = isDeleted
        self.work_id = work_id
        self.work_library_id = work_library_id
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(work_relation)

    @staticmethod
    def get_dataframe():
        return get_dataframe(work_relation)