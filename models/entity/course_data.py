from datetime import datetime
from util.db_util.db_read import get_data


class course_data:
    def __init__(self, id, insert_time: datetime, create_time: datetime, last_modify_time: datetime, type, name,
                 personid, courseid, url, size, object_id, isDeleted, data_id, fid):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.type = type
        self.name = name
        self.personid = personid
        self.courseid = courseid
        self.url = url
        self.size = size
        self.object_id = object_id
        self.isDeleted = isDeleted
        self.data_id = data_id
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(course_data)

    @staticmethod
    def get_dataframe(activity_log):
        return get_data(activity_log)
