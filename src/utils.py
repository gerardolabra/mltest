import os
import sys

import dill

from src.exception import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        logging.info(f"Attempting to save object at {file_path}")
        dir_path = os.path.dirname(file_path)
        logging.info(f"Directory path: {dir_path}")

        os.makedirs(dir_path, exist_ok=True)
        logging.info(f"Directory created if it did not exist")

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info(f"Object saved at {file_path}")

    except Exception as e:
        logging.error(f"Error saving object: {e}")
        raise CustomException(e, sys)
