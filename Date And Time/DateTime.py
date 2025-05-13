import datetime

print(datetime.datetime(2020,6,7,4,30,54,89))

print(datetime.datetime.today())
print(datetime.datetime.now())
print(datetime.datetime.now().year)

print(datetime.date(2019,7,5))
print(datetime.time(3,45,23))

b1=datetime.timedelta(days=30)
b2=datetime.timedelta(days=90)
b3=b1-b2
print(b3)
