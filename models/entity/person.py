from datetime import datetime

from util.db_util.db_read import get_data


class person:
    def __init__(self, id: str, insert_time: datetime, create_time: datetime, last_modify_time: datetime, personid: str,
                 user_name: str, login_name: str, role: str, fid: str):
        self.id = id
        self.insert_time = insert_time
        self.create_time = create_time
        self.last_modify_time = last_modify_time
        self.personid = personid
        self.user_name = user_name
        self.login_name = login_name
        self.role = role
        self.fid = fid

    @staticmethod
    def get_all():
        return get_data(person)

    @staticmethod
    def get_dataframe():
        return get_data()
