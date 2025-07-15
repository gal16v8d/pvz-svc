"""Automation constants"""

from typing import Final


BODY: Final[str] = "body"
JSON_TYPE: Final[str] = "application/json"
JSON_NODE_DETAIL: Final[str] = "detail"
JSON_NODE_MESSAGE: Final[str] = "message"
JSON_NODE_PATH: Final[str] = "path"
REQUEST_TIMEOUT: Final[int] = 5
STATUS_CODE: Final[str] = "status_code"
UNSUPPORTED_MSG: Final[str] = (
    "Did not attempt to load JSON data because the request Content-Type was not 'application/json'."
)
