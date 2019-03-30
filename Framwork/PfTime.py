#coding=utf-8

import time, calendar
import datetime as datetime

# 获取当前系统时间
def get_current_time(timeFormat='%Y-%m-%d_%H_%M_%S'):
    now = time.strftime(timeFormat, time.localtime(time.time()))
    return now

# 获取当前系统日期
def get_current_date():
    now = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    return now

# 获取几个月后或几个月前的日期
def get_date_before_after_months(strTime, months):
    dt = datetime.date(int(strTime[0:4]), int(strTime[5:7]), int(strTime[8:10]))
    month = dt.month - 1 + months
    year = dt.year + month / 12
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    dt = dt.replace(year=year, month=month, day=day)
    return str(dt.replace(year=year, month=month, day=day))

# 将时间戳转换成字符串，如：2018-04-03 09:42:59
# 注：时间戳必须为10位长度的long型
def transfer_timestamp_to_datetime(ts):
    time_local = time.localtime(ts)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt

# 将时间戳转换成字符串，如：2018-04-03
# 注：时间戳必须为10位长度的long型
def transfer_timestamp_to_date(ts):
    time_local = time.localtime(ts)
    dt = time.strftime("%Y-%m-%d", time_local)
    return dt

# 件excel中读取到的日期进行转换为python的datetime格式
def transfer_datetime(date):
    if isinstance(date, float):
        date = int(date)
    d = datetime.date.fromordinal((datetime.date(1899, 12, 31).toordinal() - 1) + date)
    return d