from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_trainer import ModelTraining
from cnnClassifier import logger


STAGE_NAME = 'Model Training Stage'

class ModelTrainingPipeline:
  def __init__(self):
    pass

  def main(self):
    config = ConfigurationManager()
    model_trainer_config = config.get_model_trainer_config()
    model_training = ModelTraining(config=model_trainer_config)
    model_training.get_base_model()
    model_training.train_valid_generator()
    model_training.train()



if __name__ == "__main__":
  try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
  except Exception as e:
    logger.exception(e)
    raise e