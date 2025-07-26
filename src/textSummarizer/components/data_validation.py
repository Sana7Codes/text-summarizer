import os
from pathlib import Path
from textSummarizer.logging import logger
from textSummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    def validate_all_files_exist(self) -> bool:
        """
        Validate if all required directories exist in the samsum_dataset directory.
        """
        try:
            validation_status = True
            dataset_dir = os.path.join("artifacts", "data_ingestion", "data", "samsum_dataset")

            for required_file in self.config.ALL_REQUIRED_FILES:
                required_path = os.path.join(dataset_dir, required_file)
                if not os.path.exists(required_path):
                    validation_status = False
                    break

            # Save status
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            return validation_status

        except Exception as e:
            logger.error(f"Error during validation: {e}")
            return False
