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
    list = []
    keys = ['text','intent','entities']
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             intent = collections.OrderedDict()
             for i in range(ncols-1):
                intent[keys[i]] = row[i]
             intent['entities'] = []
             list.append(intent)
    return list


def get_intens():
    intent = collections.OrderedDict()
    intent = get_infos.open_json('Service_identifier')
    other_intent = excel_table_byindex('./data/intents.xlsx')
    # print(other_intent)
    # return
    intent.get('utterances').extend(other_intent)
    # intent['utterances'] = intent.get('utterances') + other_intent

    with open('jsonfile/intents.json','w') as f:
        f.write(json.dumps(intent,ensure_ascii=False,indent=4))


if __name__ == '__main__':
    get_intens()