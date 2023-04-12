import os

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def get_db():
    try:
        client = MongoClient(os.environ.get('MONGO_URI'))
        db = client.testdbflask
        print('Connected to MongoDB')
    except ConnectionFailure as e:
        print(f'Connection error: {e}')
        db = None

    return db
