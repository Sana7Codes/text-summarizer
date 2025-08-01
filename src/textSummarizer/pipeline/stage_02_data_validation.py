from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Initialize Configuration Manager
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        # Initialize Data Validation
        data_validation = DataValidation(config=data_validation_config)

        # Validate all files
        data_validation.validate_all_files_exist()
       