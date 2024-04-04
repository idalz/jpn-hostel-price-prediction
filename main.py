import sys
from src.exception import CustomException
from src.logger import logging
from src.pipeline.train_pipeline import TrainPipeline

# Train Pipeline
try:
    logging.info(f"Train pipeline started.")  
    obj = TrainPipeline()
    obj.main()
    logging.info(f"Train pipeline completed.")
except Exception as e:
    CustomException(e, sys)
