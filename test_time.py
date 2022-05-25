import pandas as pd
import time


h_date = '17/05/2022 9:00:45 PM'
time_format = '%d/%m/%Y %I:%M:%S %p'
epoch_date =  int(time.mktime(time.strptime(h_date,time_format)))
print(epoch_date)
my_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(epoch_date)))
print(my_time)