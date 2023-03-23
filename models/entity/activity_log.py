from datetime import datetime

from util.db_util.db_read import get_data


class activity_log:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, dtype: str,
                 activity_id: str, personid: str, courseid: str, clazzid: str, status: str, ip: str, attend_id: str,
                 attend_time: datetime, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.dtype = dtype
        self.activity_id = activity_id
        self.personid = personid
        self.courseid = courseid
        self.clazzid = clazzid
        self.status = status
        self.ip = ip
        self.attend_id = attend_id
        self.attend_time = attend_time
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(activity_log)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)
