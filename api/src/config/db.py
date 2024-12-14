import os
from pymongo import MongoClient

from dotenv import load_dotenv
load_dotenv()

def get_db():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("DB_NAME")]
    return db