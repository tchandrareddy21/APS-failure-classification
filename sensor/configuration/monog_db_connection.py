import pymongo
from sensor.constants.database import DATABASE_NAME
import certifi
ca = certifi.where()

class MongoDBClient:
    clinet = None
    def __init__(self, database_name = DATABASE_NAME) -> None:
        try:
            if MongoDBClient.clinet is None:
                mongo_db_url = "mongodb+srv://sensor-fault-detection:sEnsOr_fAult_dEtEctIOn@sensor-fault-detection.1dmjfkb.mongodb.net/?retryWrites=true&w=majority&appName=sensor-fault-detection"
                MongoDBClient.clinet = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
            self.clinet = MongoDBClient.clinet
            self.database = self.clinet[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e