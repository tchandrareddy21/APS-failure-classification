from sensor.configuration.monog_db_connection import MongoDBClient

if __name__ == "__main__":
    mongodb_client = MongoDBClient()
    print(f"Collection Name : {mongodb_client.database.list_collection_names()}")