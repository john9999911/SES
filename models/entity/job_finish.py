from datetime import datetime

from util.db_util.db_read import get_data


class job_finish:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, job_id: str, clazzid: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.job_id = job_id
        self.clazzid = clazzid
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(job_finish)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)
