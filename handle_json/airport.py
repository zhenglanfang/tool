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
                app[i] = row[i] 
             list.append(app)
    return list


def get_airport():
    airport = collections.OrderedDict()
    airport = get_infos.open_json('airport')
    new_airport = excel_table_byindex('./data/airports.xlsx')
    # print(new_airport)
    international = airport.get('国际')
    new_dict = {}
    for item in new_airport:
        port = new_dict.get(item[0],[])
        # print(port)
        code = collections.OrderedDict()
        code['id'] = item[1]
        code['name'] = item[2]
        port.append(code)
        new_dict[item[0]] = port
    # international.update(new_dict)
    for key,value in new_dict.items():
        flag = False
        # value = {item['id']:item for item in value}
        # for air_id in value.keys():
        old_codes = [ port['id'] for value2  in international.values() for port in value2]
        new_codes = [item['id'] for item in value]
        inter_code = set(new_codes).intersection(set(old_codes))
        if inter_code :
            port_dict = {item['id']:item for item in value}
            differ_code = set(new_codes).difference(set(old_codes))
            add_data = [port_dict[k] for k in differ_code]
            # 查找原始数据的key，将不存在的数据添加进去
            for key2,value2 in international.items():
                if inter_code.intersection(set([item['id'] for item in value2])):
                    international[key2].extend(add_data)
                    break
        else:
            international[key] = value
            # for key2,value2 in international.items():
            #     for air in value2:
            #         if air_id == air['id']:
            #             # 是同一个城市
            #             flag = True
            #             break    


    airport['国际'] = international

    with open('jsonfile/new-airport.json','w') as f:
        f.write(json.dumps(airport,ensure_ascii=False,indent=4))


if __name__ == '__main__':
    get_airport()