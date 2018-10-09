# Project: Curl
# Purpose Details: Learn Curl
# Course: IST 411
# Author: Chris Valko
# Date Developed: 09/04/2018
# Last Date Changed: 09/06/2018
# Rev:1

import json, sys, urllib.parse, urllib.request, urllib.error

# https://jsonplaceholder.typicode.com/posts/1/comments
print('https://jsonplaceholder.typicode.com/posts/1/comments')
url = 'https://jsonplaceholder.typicode.com'
param = '/posts/1/comments'
try:
	#value = urllib.parse.urlencode(param)
	print('Url: ', url + param)
	response = urllib.request.urlopen(url+param)
	payload = response.read()
	payloadJSON = json.loads(payload.decode('utf-8')) 
	with open('payloadJSON.json', 'w') as outFile:
        	jsonPayload = outFile.write(json.dumps(payloadJSON))

	print('Payload: ', payload)

except:
	e = sys.exc_info()[0]
	print("error: %s" % e)
