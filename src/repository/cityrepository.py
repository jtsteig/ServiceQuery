from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from repository.servicerepository import Services
from utils.functionlogger import functionLogger

import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Cities(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    city_name = Column(String, nullable=False)

    def __init__(self, service_id, city_name):
        self.service_id = service_id
        self.city_name = city_name

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Cities).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetAll(self, session):
        return session.query(Cities).all()
    
    @functionLogger
    def Create(self, session):
        session.add(self)
        session.flush()
        session.refresh(self)
        return self


Base.metadata.create_all(engine)
