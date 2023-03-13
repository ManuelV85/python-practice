###dates###
from datetime import datetime

now = datetime.now()


def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

timestamp = now.timestamp()

print(timestamp)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023)


from datetime import time

current_time = time(14,25,3) #sobre time hay que hacer operaciones para despues acceder a sus datos
                      # es un objeto que sirve para encapsular tiempo
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#datetime agrupa fecha y hora.....date agrupa fecha..... time agrupa hora.
from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

print(current_date.year, current_date.month, current_date.day)

current_date = date(2023, 10, 12)
print(current_date)

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month) #como se puede observar, se pueden hacer operaciones 

diff = year_2023 - now
print(diff)
diff = year_2023.date() - current_date
print(diff)

from datetime import timedelta

time_delta = timedelta()

init_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks= 13)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)

