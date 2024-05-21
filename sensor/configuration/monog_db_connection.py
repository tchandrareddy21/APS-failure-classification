import pymongo
from sensor.constants.database import DATABASE_NAME
import os
import certifi
ca = certifi.where()

class MongoDBClient:
    clinet = None
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.clinet is None:
                # mongo_db_url = "USE your OWN URL"
                # MongoDBClient.clinet = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
                MongoDBClient.clinet = pymongo.MongoClient(os.env, tlsCAFile = ca)
            self.clinet = MongoDBClient.clinet
            self.database = self.clinet[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e