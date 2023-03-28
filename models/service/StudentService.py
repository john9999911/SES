import pandas as pd

from models.entity.person import person
from models.entity.activity_log import activity_log


class StudentService:
    def __init__(self, personid):
        self.personid = personid

    def getProperties(self):
        # activity_log
        stu_activity_log = activity_log.get_dataframe()
        # 在dataframe中筛选出personid等于属性student的personid的记录
        print(self.personid, type(self.personid))
        stu_activity_log = stu_activity_log[stu_activity_log['personid'] == self.personid]
        if stu_activity_log.empty:
            print(0)
            return
        print(stu_activity_log)
        # 删除status为11的记录
        stu_activity_log = stu_activity_log[stu_activity_log['status'] != 11]
        # 1.获取已完成课堂活动数cnt1和未完成课堂活动数cnt2 3为完成 其他为未完成
        stu_activity_log_1 = stu_activity_log[stu_activity_log['status'] == 3]
        cnt1 = stu_activity_log.shape[0]
        # 2.完成度为cnt/(cnt1+cnt2)
        stu_activity_log_2 = stu_activity_log[stu_activity_log['status'] != 3]
        cnt2 = stu_activity_log_2.shape[0]
        # 完成度
        finish_rate = cnt1 / (cnt1 + cnt2)
        print('完成度为：', finish_rate)


if __name__ == '__main__':
    student = person.get_dataframe()
    student = student[student['role'] == '3']
    for index, row in student.iterrows():
        StudentService(row['personid']).getProperties()
