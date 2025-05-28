"""Define possible usage values in the app"""

from enum import Enum


class Usage(str, Enum):
    """Usage values"""

    DELAYED: str = "delayed activation"
    INSTANT: str = "instant"
    ON_CONTACT: str = "on contact"
    SINGLE_USE: str = "single use"
