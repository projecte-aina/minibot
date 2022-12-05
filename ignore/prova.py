import lingua_franca
from lingua_franca.format import nice_date, nice_date_time, nice_time
from lingua_franca.time import default_timezone
import pytz
import datetime
lingua_franca.load_language('ca')

#print(nice_time(datetime.datetime.now()))
print(nice_time(datetime.datetime.now(pytz.timezone('Europe/Brussels')), variant="traditional"))
# 
print(nice_time(datetime.datetime.now(), variant="bell"))
# print(nice_time(datetime.datetime.now(), variant="full_bell"))
# print(nice_time(datetime.datetime.now(), variant="spanish"))
# print(nice_time(datetime.datetime.now(), use_24hour=True))

print(datetime.datetime.now())