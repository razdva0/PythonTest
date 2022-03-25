from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
import time as tm

d1 = date(19, 3, 12)
print(d1)
t1 = time(23, 10, 20, 32)
print(t1)
print(datetime.max)
td1 = timedelta(100, 100)
print(td1)
print(datetime.now().microsecond % 100)
tm.sleep(datetime.now().microsecond % 10 / 1_000_000)
print(datetime.now().microsecond % 100)
