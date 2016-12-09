#!/usr/bin/env python
#coding:utf8

import requests
import json
import sys

# config-start
BingKey = "adbdf06e4f38487c8a522bc8a87a220d"
keyword = sys.argv[1]
modelName = "Bing"
maxPageNumber = 10
pageSize = 10
# config-end

url = "https://api.cognitive.microsoft.com/bing/v5.0/search?q=" + keyword

headers = {
	'Host':'api.cognitive.microsoft.com',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:50.0) Gecko/20100101 Firefox/50.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
	'Accept-Encoding':'gzip, deflate, br',
	'Ocp-Apim-Subscription-Key':BingKey,
	'Upgrade-Insecure-Requests':'1',
	'Referer':'https://api.cognitive.microsoft.com/bing/v5.0/search?q=opensns',
	'Connection':'keep-alive',
}


for i in range(maxPageNumber):
	tempUrl = url + "&offset=" + str(i * pageSize) + "&count=" + str(pageSize)
	response = requests.get(tempUrl, headers=headers)
	content = response.text
	jsonObject = json.loads(content)
	results = jsonObject['webPages']['value']
	for result in results:
		resulturl = result['displayUrl']
		if resulturl.startswith("https://"):
			result_url = resulturl
		else:
			result_url = "http://" + resulturl
		print result_url
		try:
			result_file = open("../Results/" + modelName + "_" + keyword + ".txt" ,"a+")
			result_file.write(result_url + "\r\n")
			result_file.close()
		except Exception as e:
			pass

