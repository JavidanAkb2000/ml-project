import logging
import os
from datetime import datetime


today = datetime.now().strftime("%Y-%m-%d")

logs_dir = os.path.join(os.getcwd(), 'logs', today)
os.makedirs(logs_dir, exist_ok=True) 

LOG_FILE_PATH = os.path.join(logs_dir, f"{today}.log")

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
