import logging
import os
from datetime import datetime


LOG_FILENAME = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_PATH = os.path.join(os.getcwd(),"logs")
os.makedirs(LOGS_PATH,exist_ok = True)
LOG_FILENAME_PATH = os.path.join(LOGS_PATH,LOG_FILENAME)
logging.basicConfig(filename=LOG_FILENAME_PATH, level=logging.INFO, format ="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")


# if __name__ == "__main__":
#     logging.info("Logging is started")