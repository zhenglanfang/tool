# -*- coding: utf-8 -*- 

import get_infos
import xlrd
import collections
import json

def open_excel(file= 'file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print (str(e))

#根据索引获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_index：表的索引
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
                app[i] = str(row[i]) 
             list.append(app)
    return list


def get_airport():
    order_json = collections.OrderedDict()
    row_data = get_infos.open_json('alternative_names')
    other_data = excel_table_byindex('./data/other_name.xlsx')
    new_dict = {}
    for item in other_data:
        new_dict[item[0]] = [value for key,value in item.items() if not(value.strip() == '' or key == 0)]
    
    row_data['V5.4'] = new_dict
    # print(row_data)
    # return
    with open('jsonfile/new_alternative_names.json','w') as f:
        f.write(json.dumps(row_data,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    get_airport()