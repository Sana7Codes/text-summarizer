# No standard library or third-party imports required here

from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"
try: 
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:  
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation .main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer Stage"  
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e