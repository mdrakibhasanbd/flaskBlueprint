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
