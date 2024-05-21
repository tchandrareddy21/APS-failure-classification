from sensor.configuration.monog_db_connection import MongoDBClient

from sensor.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig
from sensor.logger import logging
from sensor.exception import  SensorException

if __name__ == "__main__":
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config= training_pipeline_config)
    print(data_ingestion_config.__dict__)