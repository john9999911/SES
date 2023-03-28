from datetime import datetime

from util.db_util.db_read import get_dataframe


class work_answer:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, work_id: str, status: str, answer_time: datetime, score: str, piyue_person_id: str, ip: str, piyue_time: datetime, isDeleted: str, fid: str, clazzid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.work_id = work_id
        self.status = status
        self.answer_time = answer_time
        self.score = score
        self.piyue_person_id = piyue_person_id
        self.ip = ip
        self.piyue_time = piyue_time
        self.isDeleted = isDeleted
        self.fid = fid
        self.clazzid = clazzid


    @staticmethod
    def get_dataframe():
        return get_dataframe(work_answer)
