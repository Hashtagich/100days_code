import datetime as dt

date_now = dt.datetime.now()
year = date_now.year
day_week = date_now.weekday()
print(date_now, year, day_week, sep='\n')
print()

date_of_birth = dt.datetime(year=2000, month=12, day=31)
date_of_birth_1 = dt.date(year=2000, month=12, day=31)
print(date_of_birth, date_of_birth_1, sep='\n')
