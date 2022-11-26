import pymongo


MONGO_HOST = 'localhost'
MONGO_CONN = pymongo.MongoClient(f"mongodb://{MONGO_HOST}")
