import sys, datetime
from pymongo import MongoClient
try:
    client = MongoClient('localhost', 27017)
    print("Connected to MongoDB")
    db = client.test_database
    print("Got the Database test_database")
    collection = db.test_collection
    print("Got the Collection")
    post = {"author": "Mike","text": "My first blog post!","tags": ["mongodb", "python", "pymongo"],"date": datetime.datetime.utcnow()}
    print("Created the Document object")
    post_id = collection.insert_one(post)
except:
    e = sys.exc_info()[0]
    print("error: %s" % e
