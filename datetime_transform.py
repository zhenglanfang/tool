#! /usr/bin/python
# coding:utf-8

import re
import time

from datetime import datetime
from datetime import date
# from datetime import timezone
from datetime import timedelta


class DatetimeTransfrom(object):
    """docstring for DatetimeTransfrom"""
    fmt = "%Y-%m-%d %H:%M:%S"
    
    def __init__(self):
        super(DatetimeTransfrom, self).__init__()

    @staticmethod
    def str_to_datetime(string, fmt=fmt):
        return datetime.strptime(string,fmt)

    @staticmethod
    def str_to_timestamp(string, fmt=fmt):
        return time.mktime(time.strptime(string, fmt))

    @staticmethod
    def datetime_to_str(dt, fmt=fmt):
        return dt.strftime(fmt)

    @staticmethod
    def datetime_to_timestamp(dt):
        # puthon3: dt.timestamp() 
        return time.mktime(dt.timetuple())

    @classmethod
    def datetime_to_utcdatetime(cls, dt):
        timestamp = cls.datetime_to_timestamp(dt)
        return datetime.utcfromtimestamp(timestamp)

    @classmethod
    def timestamp_to_str(cls, timestamp, fmt=fmt):
        dt = datetime.fromtimestamp(timestamp)
        return cls.datetime_to_str(dt, fmt)

    @staticmethod
    def timestramp_to_datetime(timestamp):
        return datetime.fromtimestamp(timestamp)

    @classmethod
    def utcstr_to_timestamp(cls, dt_str, tz_str, fmt=fmt):
        '''
        python3
        将日期str和时区str转换为timestamp
        :param dt_str:日期  2015-1-21 9:01:30
        :param tz_str:时区  UTC+5:00
        :param fmt:日期的格式
        :return:timestamp
        '''
        # 将字符串日期转换为datetime
        dt_str = datetime.strptime(dt_str, fmt)

        # 正则获取需要加减的时区信息(+7,-9)
        tz_str = re.match(r'UTC([+-]\d+):00', tz_str).group(1)

        # 强制设置为UTC
        dt = dt_str.replace(tzinfo=timezone(timedelta(hours=int(tz_str))))
        return dt.timestamp()

    @staticmethod
    def compare_datetime(strtime):
        '''
           判断一个字符串日期是否是当天日期
           strtime: '%Y-%m-%d %H:%M:%S' or '%Y-%m-%d'
        '''
        strtime = strtime.split()[0]
        time1 = datetime.strptime(strtime, '%Y-%m-%d')
        time1 = date(time1.year,time1.month,time1.day)
        now = date.today()
        if time1 == now:
            return True
        else:
            return False


if __name__ == '__main__':
    datetime_transfrom = DatetimeTransfrom()
    str = '2015-04-19 12:20:00'
    dt = datetime_transfrom.str_to_datetime(str)
    timestamp = datetime_transfrom.str_to_timestamp(str)
    # print(datetime_transfrom.datetime_to_str(dt))
    # print(datetime_transfrom.datetime_to_timestamp(dt))
    print(datetime_transfrom.datetime_to_utcdatetime(dt))
    print(datetime_transfrom.timestamp_to_str(timestamp))
    print(datetime_transfrom.timestramp_to_datetime(timestamp))
    # print(datetime_transfrom.utcstr_to_timestamp(str,'UTC+5:00'))