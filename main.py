from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os
from sensor.pipeline.batch_prediction import start_batch_prediction
from sensor.pipeline.training_pipeline import start_training_pipeline
file_path="/config/workspace/aps_failure_training_set1.csv"
if __name__=="__main__":
     try:
          output_file=start_batch_prediction(input_file_path=file_path)
          print(output_file)
          #start_training_pipeline()
     except Exception as e:
          print(e)