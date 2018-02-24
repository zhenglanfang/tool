# coding:utf-8

import json
import collections

from get_infos import get_infos

def get_exclude_json():
    '''
    {
      "text": "别！",
      "intent": "cancel",
      "entities": []
    }
    '''
    encludes = get_infos('exclude')
    enclude_json = []
    for item in encludes:
        item_dict = {}
        item_dict['text'] = item
        item_dict['intent'] = 'cancel'
        item_dict['entities'] = []
        enclude_json.append(item_dict)
    print(len(enclude_json))
    with open('jsonfile/exclude.json','w') as f:
        f.write(json.dumps(enclude_json,ensure_ascii=False))

def get_airline_json():
	'''
	{
      "text": "不想坐东航，换深航吧",
      "intent": "form",
      "entities": [
        {
          "entity": "airline",
          "startPos": 3,
          "endPos": 4
        },
        {
          "entity": "airline",
          "startPos": 7,
          "endPos": 8
        },
        {
          "entity": "exclude",
          "startPos": 0,
          "endPos": 2
        }
      ]
    }
	'''
	airlines = get_infos('airline')
	tones = get_infos('exclude')
	items = get_infos('cancel')
	item_json = []
	for item in items:
		item_dict = collections.OrderedDict()
		item_dict['text'] = item
		item_dict['intent'] = 'form'
		item_dict['entities'] = []
		
		for airline in airlines:
			startPos = item.find(airline)
			# print(startPos)
			if startPos > -1:
				entity  = collections.OrderedDict()
				entity['entity'] = 'airline'
				entity['startPos'] = startPos
				entity['endPos'] = startPos + len(airline)-1
				item_dict['entities'].append(entity)
				break

		for tone in tones:
			startPos = item.find(tone)
			if startPos > -1:
				entity  = collections.OrderedDict()
				entity['entity'] = 'exclude'
				entity['startPos'] = startPos
				entity['endPos'] = startPos + len(tone)-1
				item_dict['entities'].append(entity)
				break
				
		# print(item_dict)
		# break
		item_json.append(item_dict)

	print(len(item_json))
	return item_json
	
	with open('jsonfile/airline.json','w') as f:
		s = json.dumps(item_json,ensure_ascii=False,indent=4)
		f.write(s)

if __name__ == '__main__':
	# get_exclude_json()
	get_airline_json()