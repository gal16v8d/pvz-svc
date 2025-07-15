"""Base config for automation tests, define target and other basic config"""

import json
import os
from typing import Any

from dotenv import dotenv_values, find_dotenv


PVZ_BASE_URL = "PVZ_BASE_URL"


def load_dev_base_url() -> str:
    """
    Load the base url for test purposes from env file
    """
    env_file = find_dotenv(".env")
    config = dotenv_values(env_file)
    return config.get(PVZ_BASE_URL, "please define PVZ_BASE_URL env var")


def get_base_url() -> str:
    """
    Get the base url of service to hit and test
    """
    return (
        os.getenv(PVZ_BASE_URL)
        if os.getenv(PVZ_BASE_URL) == "prod"
        else load_dev_base_url()
    )


def load_json(file_path: str) -> Any:
    """Load json data based on path"""
    with open(file_path, encoding="utf-8") as file:
        return json.load(file)
