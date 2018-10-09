import sys
import time

from pymongo import MongoClient


class Logger:
    # time formatter
	__time = time.strftime("%Y-%m-%d %I:%M:%S %p")

	def log(self, msg):
		"""
		Log `msg` to MongoDB log
		"""

	try:
            # connect to mongoDB
		client = MongoClient('localhost', 27017)
		db = client.db_group4
		collection = db.log_group4
		entry = {'timestamp': self.__time, 'msg': msg}
            # insert the entry
		collection.insert_one(entry)

	except:
		e = sys.exc_info()[0]
		print("error: %s" % e)
	def display_log(self):
		"""
		displays the log file in MongoDB
		"""

	try:
            # connect to MongoDB
		from pprint import pprint
		client = MongoClient('localhost', 27017)
		db = client.db_group4
		collection = db.log_group4
            # read from the collection
		cursor = collection.find({})
		for document in cursor:
			pprint(document)

	except:
		e = sys.exc_info()[0]
		print("error: %s" % e)
