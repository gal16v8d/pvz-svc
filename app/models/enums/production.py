"""Define possible production values in the app"""

from enum import Enum


class Production(str, Enum):
    """Plant production args"""

    DOUBLE: str = "double"
    LOW: str = "low"
    NORMAL: str = "normal"
