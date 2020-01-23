from datetime import datetime, timedelta
particular_date = datetime(1988, 8, 9)
new_date = datetime.today() - particular_date
print (new_date.days)