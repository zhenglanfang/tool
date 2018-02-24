#! /usr/bin/python
# coding:utf-8

import json
import xlrd
import xlwt
import xlutils
import collections

from xlutils.copy import copy

from collections import OrderedDict

# 读取文本
def get_infos(file_name):
	items = []
	with open('data/%s.txt' % file_name, 'r') as f:
	    for line in f.readlines():
	        item = line.strip()
	        items.append(item)
	return items

# 读取json 文件，并保持原有格式
def open_json(file_name):
	with open('jsonfile/%s.json'%file_name,'r') as f:
		s = f.read()
		j = json.loads(s,object_pairs_hook=OrderedDict)
		# print(j.keys()[0])
	return j

# 打开excel文件
def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print (str(e))

#根据索引获取Excel表格中的数据   
# 参数:file：Excel文件路径     
# colnameindex：表头列名所在行的
# by_index：表的索引
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    # colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(ncols):
                app[i] = row[i] 
             list.append(app)
    return list

# 返回以colnames为key
def excel_table_byindex(file= 'file.xls',colnameindex=0,by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows #行数
    ncols = table.ncols #列数
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for v,i in enumerate(colnames):
                app[v] = row[i] 
             list.append(app)
    return list


# 创建新的excel
def write_excel(file):
    # 创建工作簿
    f = xlwt.Workbook() 
    # 创建一个 user_info 的 sheet
    sheet1 = f.add_sheet(u'user_info',cell_overwrite_ok=True)
    rows = [['姓名', '性别', '年龄', '身高', '体重'],
              ['张三', '男', '18', '166', '60'],
              ['李四', '未知', '未知', '177', '88']]
    for i in xrange(len(rows)):
        row = rows[i]
        for j in xrange(len(row)):
            # 以 cell 为单位写出单元格
            sheet1.write(i, j, rows[i][j])
    # 保存
    f.save('/Users/imaygou/Code/test/test.xls')


# 修改excel
def modify_excel(file):
    # old_excel=xlrd.open_workbook('data/%s'%file, formatting_info=True)  
    old_excel = xlrd.open_workbook('data/%s'%file)
    old_sheet = old_excel.sheets()[0]  
    new_wb = copy(old_excel)
    new_ws = new_wb.get_sheet(0)
    for i in range(1,old_sheet.nrows):
        value = old_sheet.cell(i,2).value
        # print(value)
        ncols = old_sheet.ncols
        new_ws.write(i,ncols+1,'test')

    new_wb.save('data/test.xls')


if __name__ == '__main__':
	# citys = get_infos('city')
	# print(citys[1])
	# open_json('Flight-Tickets')
    modify_excel('airport.xlsx')
