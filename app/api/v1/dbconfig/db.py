# import pymongo
# from pymongo import MongoClient
# import os
# from dotenv import load_dotenv
# load_dotenv()
#
# mongoUri = os.getenv("mongoUri")
# mongoport = os.getenv("mongoport")
# mongoDatabase = os.getenv("mongoDatabase")
#
# mongo_client = MongoClient(mongoUri, int(mongoport))
# db = mongo_client.get_database(mongoDatabase)

import pymongo
from pymongo import MongoClient
import os
from dotenv import load_dotenv

def get_mongo_db():
    load_dotenv()

    mongoUri = os.getenv("mongoUri")
    mongoport = os.getenv("mongoport")
    mongoDatabase = os.getenv("mongoDatabaseName")

    mongo_client = MongoClient(mongoUri, int(mongoport))
    db = mongo_client.get_database(mongoDatabase)

    return db

# # Usage
# if __name__ == "__main__":
#     my_db = get_mongo_db()
#     collection = my_db["my_collection"]

    # Perform database operations using the 'collection' object
    # For example: collection.insert_one({"key": "value"})

