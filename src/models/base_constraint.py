'''Allow to define constraints in db'''
from typing import List
from pymongo import database, ASCENDING


class BaseConstraint:
    '''Allow to define constraints in db'''

    def __init__(self, db: database.Database,
                 collection: str, attribs: List[str]) -> None:
        self.db = db
        self.collection = collection
        self.attribs = attribs

    def create_indexes(self):
        '''Create all the related indexes for the collection'''
        for attribute in self.attribs:
            self.db[self.collection].create_index(
                [(attribute, ASCENDING)],
                unique=True
            )
