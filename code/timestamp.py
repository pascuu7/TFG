import time
from xmlrpc.client import _iso8601_format
import datetime
# s = "03/04/2012 18:00:06"
# hola = time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y %H:%M:%S").timetuple())

# print(hola)

t = "03/04/2012 18:00:06"
hola = int(datetime.datetime.strptime('03/04/2012 18:00:06', '%d/%m/%Y %H:%M:%S').strftime("%s"))

print(hola)
# 4f5e3a72e4b053fd6a4313f6 Tue Apr 03 18:00:06 +0000 2012	240  MOSCU