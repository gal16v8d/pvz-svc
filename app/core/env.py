"""Define env load"""

import os

from app.consts import env


current_env = os.getenv(env.PVZ_ENV)
