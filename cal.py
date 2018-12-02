import time
import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print('Current date and time: ', now)
print('Current year: ', today.strftime("%Y"))
print('Month of the year: ', today.strftime("%B"))
print('Week of the year: ', today.strftime("%W"))
print('Weekday of the week: ', today.strftime("%w"))
print('Day of the year: ', today.strftime("%j"))
print('Day of the month: ', today.strftime("%d"))
print('Day of the week: ', today.strftime("%A"))
