from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates
from service.db_base import Base, engine
from schema.validations import Validations
from repository.servicerepository import Services
from utils.functionlogger import functionLogger

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Hours(Base):
    __tablename__ = 'hours'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    day_of_week = Column(String, nullable=False)
    open_at = Column(Integer, nullable=False)
    close_at = Column(Integer, nullable=False)

    def __init__(self, day_of_week, open_at, close_at):
        self.day_of_week = day_of_week
        self.open_at = open_at
        self.close_at = open_at

    @validates('open_at')
    def validates_open_at(self, key, open_at):
        return Validations.validate_service_hour(self, key, open_at)

    @validates('close_at')
    def validates_close_at(self, key, close_at):
        return Validations.validate_service_hour(self, key, close_at)

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Hours).delete()
        session.flush()


Base.metadata.create_all(engine)
