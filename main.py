from plant.pipeline.stage_01_pipeline import DataIngestionTrainingPipeline
from plant import logger


STAGE_NAME = 'Data Ingestion Stage'
try:
    logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
