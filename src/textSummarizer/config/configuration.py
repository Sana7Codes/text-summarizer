from pathlib import Path
from textSummarizer.constants import *
from textSummarizer.entity import DataIngestionConfig
from textSummarizer.entity import DataValidationConfig
from textSummarizer.entity import DataTransformationConfig
from textSummarizer.utils.common import read_yaml, create_directories



class ConfigurationManager:
    def __init__(self, config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([Path(self.config.artifacts_root)])
    
    # Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([Path(config.root_dir)])
         
        return DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL, 
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config         
    


      # Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([Path(config.root_dir)])
         
        return DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=Path(config.STATUS_FILE),
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([Path(config.root_dir)])

        return DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            tokenizer_name=Path(config.tokenizer_name)
        )

        return data_validation_config