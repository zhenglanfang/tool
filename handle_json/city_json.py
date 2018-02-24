#! /usr/bin/python
# coding:utf-8

import json
import collections

from get_infos import get_infos
from get_infos import open_json
from airline import get_airline_json

citys = get_infos('city')

def get_city_json():
    '''
        {
          "text": "上海",
          "intent": "form",
          "entities": [
            {
              "entity": "地址",
              "startPos": 0,
              "endPos": 1
            }
          ]
        },
    '''
    citys = get_infos('city')
    citys_json = []
    for city in citys:
        city_dict = collections.OrderedDict()
        city_dict['text'] = city
        city_dict['intent'] = 'form'
        entity = collections.OrderedDict()
        entity = {
          'entity':'地址',
          'startPos':0,
          'endPos':len(city)-1,
        }
        city_dict['entities'] = [entity]
        citys_json.append(city_dict)

    return citys_json
    # with open('jsonfile/city.json','w') as f:
    #     f.write(json.dumps(citys_json,ensure_ascii=False))

def get_start_json(item):
    '''
       {
          "text": "打算从北京",
          "intent": "form",
          "entities": [
            {
              "entity": "地址::出发地",
              "startPos": 3,
              "endPos": 4
            }
          ]
        } 
    '''
    for city in citys:
        item = item.upper()
        city = city.upper()
        if item.find(city)>-1:
            startPos = item.find(city)
            endPos = startPos + len(city) -1
            break
    en = collections.OrderedDict()
    en["entity"] =  "地址::出发地"
    en["startPos"] = startPos
    en["endPos"] = endPos
    entity = [en]

    return entity 

def get_end_json(item):
    '''
        {
          "text": "我要去上海",
          "intent": "form",
          "entities": [
            {
              "entity": "地址::目的地",
              "startPos": 3,
              "endPos": 4
            }
          ]
        },
    '''
    for city in citys:
        item = item.upper()
        city = city.upper()
        if item.find(city)>-1:
            startPos = item.find(city)
            endPos = startPos + len(city) -1
            break

    en = collections.OrderedDict()
    en["entity"] =  "地址::目的地"
    en["startPos"] = startPos
    en["endPos"] = endPos
    entity = [en]

    return entity
     
def start_end_json(item):
    '''
        {
          "text": "明天北京飞上海",
          "intent": "form",
          "entities": [
            {
              "entity": "地址::出发地",
              "startPos": 2,
              "endPos": 3
            },
            {
              "entity": "地址::目的地",
              "startPos": 5,
              "endPos": 6
            }
          ]
        }
    '''
    entities = []
    for city in citys:
        if len(entities) > 1:
            break
        item = item.upper()
        city = city.upper()
        if item.find(city)>-1:
            startPos = item.find(city)
            endPos = startPos + len(city) -1
            entity = collections.OrderedDict()
            entity = {
                "entity": "地址::出发地",
                "startPos": startPos,
                "endPos": endPos
            }
            entities.append(entity)
    
    if len(entities) > 1:
        if entities[0]['startPos'] > entities[1]['startPos']:
            entities[0]['entity'] = '地址::目的地'
        else:
            entities[1]['entity'] = '地址::目的地'
    else:
        print(item)
        return
    return entities

def end_start_json(item):
    entities = []
    for city in citys:
        if len(entities) > 1:
            break
        item = item.upper()
        city = city.upper()
        if item.find(city)>-1:
            startPos = item.find(city)
            endPos = startPos + len(city) -1
            entity = collections.OrderedDict()
            entity = {
                "entity": "地址::出发地",
                "startPos": startPos,
                "endPos": endPos
            }
            entities.append(entity)
    
    if len(entities) > 1:
        if entities[0]['startPos'] < entities[1]['startPos']:
            entities[0]['entity'] = '地址::目的地'
        else:
            entities[1]['entity'] = '地址::目的地'
    else:
        print(item)
        return
    return entities


def get_json(types):
    citys = get_infos('city')
    items = get_infos(types)
    start_jsons = []
    for item in items:
        start_json = collections.OrderedDict()
        start_json['text'] = item
        start_json['intent'] = 'form'
        
        if types == 'start':
            entities= get_start_json(item)
        elif types == 'end':
            entities = get_end_json(item)
        elif types == 'start_end':
            entities = start_end_json(item)
        elif types == 'end_start':
            entities = end_start_json(item)
        else:
            print('types error')
            return

        start_json['entities'] =  entities              
        start_jsons.append(start_json)

    print(len(start_jsons))    
    return start_jsons
    # with open('jsonfile/%s.json'%types,'w') as f:
    #     f.write(json.dumps(start_jsons,ensure_ascii=False,indent=4,sort_keys=True))


if __name__ == '__main__':
    city = get_city_json()
    start = get_json('start')
    end = get_json('end')
    start_end = get_json('start_end')
    end_start = get_json('end_start')
    apirport = get_airline_json()
    json_data = start + end + start_end + end_start + apirport + city
    row_data = collections.OrderedDict()
    row_data = open_json('Flight-Tickets')
    row_data['utterances'].extend(json_data)
    with open('jsonfile/json-data3.json','w') as f:
        f.write(json.dumps(row_data,ensure_ascii=False,indent=4))


   

