#Project: Mongodb
#Purpose Details: Learn how to create and write to a mongodb
#Course: IST411
#Author: Chris Valko
#Date Developed: 09/14/2018
#Last Date Changed: 09/14/2018
#Rev: 1

import json, sys, urllib.parse, urllib.request, urllib.error
from pymongo import MongoClient

url = "https://jsonplaceholder.typicode.com"
param = "/posts/1/comments"
try:
	client = MongoClient('localhost', 27017)
	print("Connected to MongoDB")
	db = client.dbValko
	print("Got the Database dbValko")
	collection = db.collectionValko
	print("Got the Collection")
	response = urllib.request.urlopen(url+param)
	mongoJSON = response.read()
	print("Created the Document object")
	collectionPrint = json.loads(mongoJSON.decode('utf-8'))
	post_id = collection.insert(collectionPrint)
except:
	e = sys.exc_info()[0]
	print("error: %s" % e)
