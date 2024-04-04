from src.logger import logging
from src.pipeline.train_pipeline import TrainPipeline
# Train Pipeline
try:
    logging.info(f"Train pipeline started.")  
    obj = TrainPipeline()
    obj.main()
    logging.info(f"Train pipeline completed.")
except Exception as e:
    raise e
