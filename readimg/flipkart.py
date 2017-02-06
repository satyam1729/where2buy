#u can add price comparision for lower price search


def flipkartsearch(text):
	import json
	import requests
	headers = {'Fk-Affiliate-Id':'satyam66h','Fk-Affiliate-Token':'1454d0d14f774904a1c9bc2a7b924923'}
	url='https://affiliate-api.flipkart.net/affiliate/1.0/search.json?query='+text+'&resultCount=1'
	r = requests.get(url, headers=headers).json()
	title=r['productInfoList'][0]['productBaseInfoV1']['title']
	price=r['productInfoList'][0]['productBaseInfoV1']['flipkartSpecialPrice']['amount']
	currency=r['productInfoList'][0]['productBaseInfoV1']['flipkartSpecialPrice']['currency']
	link=r['productInfoList'][0]['productBaseInfoV1']['productUrl']
	return title,price,currency,link	
#print flipkartsearch('sony+mobile')