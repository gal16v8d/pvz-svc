"""Decorator in use by the steps to validate and return PASSED/FAILED"""

from collections.abc import Callable
import functools
from typing import Any

import requests


def rest_call_validator(func: Callable) -> Callable:
    """Fun to annotate automation test cases"""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except (
            requests.exceptions.RequestException,
            requests.exceptions.HTTPError,
            requests.exceptions.ConnectionError,
        ) as exc:
            return exc

    return wrapper
