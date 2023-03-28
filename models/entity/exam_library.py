from datetime import datetime
from util.db_util.db_read import get_data


class exam_library:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str, courseid: str, title: str, isDeleted: str, paper_library_id: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.courseid = courseid
        self.title = title
        self.isDeleted = isDeleted
        self.paper_library_id = paper_library_id
        self.fid = fid


    @staticmethod
    def get_dataframe():
        return get_dataframe(exam_library)