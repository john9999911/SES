from datetime import datetime

from util.db_util.db_read import get_data


class bbs_log:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, clazzid: str, bbs_id: str, topic_id: str, parent_id: str, role: str, reply_id: str, ip: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.clazzid = clazzid
        self.bbs_id = bbs_id
        self.topic_id = topic_id
        self.parent_id = parent_id
        self.role = role
        self.reply_id = reply_id
        self.ip = ip
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(bbs_log)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)