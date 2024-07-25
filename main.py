from cnnClassifier import logger
from cnnClassifier.pipelines.stage01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipelines.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline


STAGE_NAME = 'Data Ingestion stage'
try:
  logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
  obj = DataIngestionTrainingPipeline()
  obj.main()
  logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
  logger.exception(e)
  raise e


STAGE_NAME = 'Prepare Base Model Stage'
try:
  logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
  obj = PrepareBaseModelTrainingPipeline()
  obj.main()
  logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
  logger.exception(e)
  raise e