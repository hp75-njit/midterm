import logging
import os

# Configure log level and file path from environment variables, with defaults
LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
LOG_FILE = os.getenv("LOG_FILE", "logs/calculator.log")

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),      # Log to file
        logging.StreamHandler()             # Log to console
    ]
)
logger = logging.getLogger(__name__)