#! /usr/bin/python
# coding:utf-8

import db_mysql
import util

def update_type():
	offers = util.excel_table_byindex('./data/offers.xls')
	for offer in offers:
		name = offer[0]
		offer_type = offer[1]
		sql = "update offers set offer_type='%s' where offer_name='%s'"%(offer_type,name)
		result = db_mysql.edit(sql)
		if result == 0:
			print(sql)

if __name__ == '__main__':
	update_type()
