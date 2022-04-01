import datetime
import pandas
#print(dir(datetime))
'''
gvr=datetime.date(1956,1,31)
print(gvr)
print(gvr.year)
print(gvr.month)
print(gvr.day)

tday=datetime.date(2022,4,1)
dt=datetime.timedelta(100)
print(tday-dt)
'''

tday=datetime.datetime.today()
#print(tday)
print(tday.strftime("%H:%M:%S %p %A, %B %d, %Y"))

print(datetime.date.today())

