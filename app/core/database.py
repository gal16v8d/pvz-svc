"""Database init logic"""

import os

from dotenv import dotenv_values, find_dotenv
from pymongo import MongoClient

from app.consts import env
from app.core.env import current_env


if current_env == env.PROD_ENV:
    db_url = os.getenv(env.DB_PVZ)
else:
    env_file = find_dotenv(env.ENV_FILE)
    config = dotenv_values(env_file)
    db_url = config[env.DB_PVZ]

print(f"db_url is defined? {db_url is not None}")
pvz_database = MongoClient(db_url)
pvz_database = pvz_database.get_default_database()
