from datetime import datetime
from util.db_util.db_read import get_data


class exam_answer:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, exam_id: str, status: str, answer_time: datetime, score: str, piyue_person_id: str, ip: str, piyue_time: datetime, isDeleted: str, fid: str, clazzid: str, answerid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.exam_id = exam_id
        self.status = status
        self.answer_time = answer_time
        self.score = score
        self.piyue_person_id = piyue_person_id
        self.ip = ip
        self.piyue_time = piyue_time
        self.isDeleted = isDeleted
        self.fid = fid
        self.clazzid = clazzid
        self.answerid = answerid

    @staticmethod
    def get_all():
        return get_data(exam_answer)

    @staticmethod
    def get_dataframe():
        return get_dataframe(exam_answer)