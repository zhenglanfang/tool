# -*- coding: utf-8 -*- 

import get_infos
import xlrd
import collections
import json

def update_json():
	json1 = collections.OrderedDict()
	json1 = get_infos.open_json('test1')
	json2 = collections.OrderedDict()
	json2 = get_infos.open_json('test2')
	utterances1_dict = {i['text']:i for i in json1.get('utterances')}	

	utterances2_dict = {i['text']:i for i in json2.get('utterances')}

	utterances2_dict.update(utterances1_dict)

	json2['utterances'] = [value for value in utterances2_dict.values()]
	with open('jsonfile/json2.json','w') as f:
		f.write(json.dumps(json2,ensure_ascii=False,indent=4))


if __name__ == '__main__':
	update_json()