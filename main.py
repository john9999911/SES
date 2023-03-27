from models.entity.activity_log import activity_log

data = activity_log.get_dataframe()
for d in data:
    print(d.id)
