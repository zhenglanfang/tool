#! /usr/bin/python
# coding:utf-8

import json

from get_infos import get_infos

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
        city_dict = {}
        city_dict['text'] = city
        city_dict['intent'] = 'form'
        entity = {
          'entity':'地址',
          'startPos':0,
          'endPos':len(city),
        }
        city_dict['entities'] = [entity]
        citys_json.append(city_dict)

    with open('jsonfile/city.json','w') as f:
        f.write(json.dumps(citys_json,ensure_ascii=False))

def get_start_json():
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
    items = get_infos('start')
    start_jsons = []
    for item in items:
        start_json = {}
        start_json['text'] = item
        start_json['intent'] = 'form'
        start_json['entities'] = []
        
        for city in citys:
            item.upper()
            if item.find(city.upper())>-1:
                startPos = item.find(city)
                endPos = startPos + len(city) -1
                break

        entity = {
            "entity": "地址::出发地",
            "startPos": startPos,
            "endPos": endPos
        }
        start_json['entities'].append(entity)
        # print(json.dumps(start_json,ensure_ascii=False))
        # break
        start_jsons.append(start_json)

        with open('jsonfile/start.json','w') as f:
            f.write(json.dumps(start_jsons,ensure_ascii=False))

def get_end_json():
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
    items = get_infos('destination')
    start_jsons = []
    for item in items:
        start_json = {}
        start_json['text'] = item
        start_json['intent'] = 'form'
        start_json['entities'] = []
        
        for city in citys:
            item.upper()
            if item.find(city.upper())>-1:
                startPos = item.find(city)
                endPos = startPos + len(city) -1
                break

        entity = {
            "entity": "地址::目的地",
            "startPos": startPos,
            "endPos": endPos
        }
        start_json['entities'].append(entity)
        # print(json.dumps(start_json,ensure_ascii=False))
        # break
        start_jsons.append(start_json)

        with open('jsonfile/end.json','w') as f:
            f.write(json.dumps(start_jsons,ensure_ascii=False))

def start_end_json():
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
    items = get_infos('start_end')
    start_jsons = []
    for item in items:
        start_json = {}
        start_json['text'] = item
        start_json['intent'] = 'form'
        start_json['entities'] = []
        
        for city in citys:
            if len(start_json['entities']) > 1:
                break
            item = item.upper()
            city = city.upper()
            if item.find(city)>-1:
                startPos = item.find(city)
                endPos = startPos + len(city) -1
                entity = {
                    "entity": "地址::出发地",
                    "startPos": startPos,
                    "endPos": endPos
                }
                start_json['entities'].append(entity)
        
        entities = start_json['entities']
        if len(entities) > 1:
            if entities[0]['startPos'] > entities[1]['startPos']:
                entities[0]['entity'] = '地址::目的地'
            else:
                entities[1]['entity'] = '地址::目的地'
        else:
            print(item)
            return
        # print(json.dumps(start_json,ensure_ascii=False))
        # break
        start_jsons.append(start_json)
    print(len(start_jsons))
    with open('jsonfile/start_end.json','w') as f:
        f.write(json.dumps(start_jsons,ensure_ascii=False))

def end_start_json():
    items = get_infos('end_start')
    start_jsons = []
    for item in items:
        start_json = {}
        start_json['text'] = item
        start_json['intent'] = 'form'
        start_json['entities'] = []
        
        for city in citys:
            if len(start_json['entities']) > 1:
                break
            item = item.upper()
            city = city.upper()
            if item.find(city)>-1:
                startPos = item.find(city)
                endPos = startPos + len(city) -1
                entity = {
                    "entity": "地址::出发地",
                    "startPos": startPos,
                    "endPos": endPos
                }
                start_json['entities'].append(entity)
        
        entities = start_json['entities']
        if len(entities) > 1:
            if entities[0]['startPos'] < entities[1]['startPos']:
                entities[0]['entity'] = '地址::目的地'
            else:
                entities[1]['entity'] = '地址::目的地'
        else:
            print(item)
            return

        start_jsons.append(start_json)
    print(len(start_jsons))
    with open('jsonfile/end_start.json','w') as f:
        f.write(json.dumps(start_jsons,ensure_ascii=False))



if __name__ == '__main__':
    # get_city_json()
    # get_start_json()
    # get_end_json()
    # start_end_json()
    end_start_json()


   

