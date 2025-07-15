"""Database init logic"""

import logging
import os

from dotenv import dotenv_values, find_dotenv
from pymongo import MongoClient

from app.consts import env
from app.configs.log_cfg import LOG_NAME
from app.core.env import current_env
from app.models import all_models


log = logging.getLogger(LOG_NAME)


if current_env == env.PROD_ENV:
    db_url = os.getenv(env.DB_PVZ)
else:
    env_file = find_dotenv(env.ENV_FILE)
    config = dotenv_values(env_file)
    db_url = config[env.DB_PVZ]

log.info("db_url is defined? %s", db_url is not None)
pvz_database = MongoClient(db_url, uuidrepresentation="standard")
pvz_database = pvz_database.get_default_database()
log.info("Connected to the MongoDB database!")
# Create all the db indexes if needed
for model in all_models:
    model(pvz_database).create_indexes()
log.info("Indexes updated!")
