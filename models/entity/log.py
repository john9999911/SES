from datetime import datetime

from util.db_util.db_read import get_data


class log:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, clazzid: str, type: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.clazzid = clazzid
        self.type = type
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(log)

    @staticmethod
    def get_dataframe():
        return get_data()