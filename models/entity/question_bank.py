from datetime import datetime

from util.db_util.db_read import get_data


class question_bank:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, title: str, isDeleted: str, question_id: str, type: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.title = title
        self.isDeleted = isDeleted
        self.question_id = question_id
        self.type = type
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(question_bank)

    @staticmethod
    def get_dataframe():
        return get_data()