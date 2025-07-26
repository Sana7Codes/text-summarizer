from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize Configuration Manager
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        # Initialize Data Ingestion
        data_ingestion = DataIngestion(config=data_ingestion_config)

        # Download and extract data
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

    
    

