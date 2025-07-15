"""Logger config"""

import logging
from typing import Final

from app.consts import env
from app.core.env import current_env


LOG_NAME: Final[str] = "pvz"
LOG_LEVEL = logging.INFO
LOG_FILE: Final[str] = f"{LOG_NAME}.log"


log = logging.getLogger(LOG_NAME)
log.setLevel(LOG_LEVEL)

# Create a formatter and set it for the file handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Create a console handler and set its level and formatter
console_handler = logging.StreamHandler()
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(formatter)
log.addHandler(console_handler)

# Create a file handler and set the log level
if current_env != env.PROD_ENV:
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(LOG_LEVEL)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)
