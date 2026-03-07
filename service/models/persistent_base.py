"""
Persistent Base class for database CRUD functions
"""

import logging
from abc import abstractmethod
from flask_sqlalchemy import SQLAlchemy

logger = logging.getLogger("flask.app")

db = SQLAlchemy()


class DataValidationError(Exception):
    """Used for data validation errors when deserializing"""


class PersistentBase:
    """Base class added persistent methods"""

    def __init__(self):
        self.id = None  # pylint: disable=invalid-name

    @abstractmethod
    def serialize(self) -> dict:
        """Convert an object into a dictionary"""

    @abstractmethod
    def deserialize(self, data: dict) -> None:
        """Convert a dictionary into an object"""

    def create(self) -> None:
        """Creates a record in the database"""
        logger.info("Creating %s", self)
        self.id = None
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            logger.error("Error creating record: %s", error)
            raise DataValidationError(error) from error

    def update(self) -> None:
        """Updates a record in the database"""
        logger.info("Updating %s", self)
        try:
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            logger.error("Error updating record: %s", error)
            raise DataValidationError(error) from error

    def delete(self) -> None:
        """Removes a record from the database"""
        logger.info("Deleting %s", self)
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            logger.error("Error deleting record: %s", error)
            raise DataValidationError(error) from error

    @classmethod
    def all(cls):
        """Returns all records"""
        logger.info("Processing all records")
        return cls.query.all()

    @classmethod
    def find(cls, by_id):
        """Finds a record by its ID"""
        logger.info("Processing lookup for id %s ...", by_id)
        return cls.query.session.get(cls, by_id)
