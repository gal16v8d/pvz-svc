from typing import Any
from pymongo import ASCENDING


class BaseConstraint:

    def __init__(self, db: Any, collection: str, attrib: str) -> None:
        self.db = db
        self.collection = collection
        self.attrib = attrib

    def create_indexes(self):
        self.db[self.collection].create_index(
            [(self.attrib, ASCENDING)],
            unique=True
        )
