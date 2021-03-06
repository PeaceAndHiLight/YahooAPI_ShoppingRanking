#coding:utf-8

import sys
import urllib
import json

def yapi_topics():
	url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/json/queryRanking?'
	appid = ''
	params = urllib.urlencode(
			{'appid': appid,
			 'hits': 5,})
	
	print url + params
	response = urllib.urlopen(url + params)
	return response.read()

def do_json(s):
	data = json.loads(s)
	#print(json.dumps(data, sort_keys=True, indent=4)); sys.exit()

    #この時点でディクショナリ型になるということか？
    #jsonの階層の"Result"以下を辞書にする。keyは番号：その次の配列がvalueになっている
	item_list = data["ResultSet"]["0"]["Result"]
	#print(json.dumps(item_list, sort_keys=True, indent=4))

    #keyは番号その他になる。番号ならソートしやすいし、その他なら例外の処理をいれればよい
	#print item_list.keys()	

    #空のディクショナリを作る
	ranking = {}
	for  k, v in item_list.iteritems():
		try:
			rank = int(v["_attributes"]["rank"])
			vector = v["_attributes"]["vector"]
			query = v["Query"]
			ranking[rank] = [vector, query]
		except:
			if k == "RankingInfo":
				StartDate = v["StartDate"]
				EndDate = v["EndDate"]

	print u"集計開始日:", StartDate
	print u"集計終了日:", EndDate
	print '-' * 40
	ranking_keys = list(ranking.keys())
	ranking_keys.sort()
	for i in ranking_keys:
		print i, ranking[i][0], ranking [i][1]

if __name__ == '__main__':
	json_str = yapi_topics()
	do_json(json_str)


