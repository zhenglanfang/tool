import util

def get_cuisine():
	cuisine = util.open_json('cuisine')
	cuisine = cuisine.get('RECORDS')
	cuisine_set = set()
	for item in cuisine:
		cuisine_set.update(item['cuisine'].split(';'))


	with open('data/cuisine.txt','w') as f:
		for item in cuisine_set:
			f.write(item + '\n')


get_cuisine()