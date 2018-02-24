#!/usr/bin/python  
#coding=utf-8  

import os
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# conn=MySQLdb.connect(host="121.201.13.116",port=3306,user="essential",passwd="Essential2015",db="guanjia_beta",charset="utf8")
conn=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root",db="miqilin",charset="utf8")

# sql = "SELECT file_name FROM t_resource_info WHERE res_type = 1 AND GROUP_ID = 1 AND RESOURCE_SIZE_INT >10000000 ORDER BY CREATE_TIME LIMIT 1000"
# n = cursor.execute(sql)
# for row in cursor.fetchall():
#         file_id = row[0]
#         file_id_2 = file_id[:2]
#         path = "/Material/"+file_id_2+"/"+file_id
#         if os.path.exists(path):
#                 print "正在删除文件："+path
#                 os.remove(path)
#         else:
#                 print "未找到文件："+path
# print "完成"
# cursor.close()

def edit(sql):
	cursor=conn.cursor()
	result = cursor.execute(sql)
	conn.commit()
	# print(result)
	cursor.close()
	return result

def findall(sql):
	cursor=conn.cursor()
	cursor.execute(sql)
	result = cursor.fetchall()
	cursor.close()
	return result

def findone(sql):
	cursor=conn.cursor()
	cursor.execute(sql)
	result = cursor.fetchone()
	cursor.close()
	return result

# def exsist()