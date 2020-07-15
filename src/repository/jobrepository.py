from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from repository.servicerepository import Services
from utils.functionlogger import functionLogger

import datetime
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    job_name = Column(String, nullable=False)

    def __init__(self, service_id, job_name):
        self.service_id = service_id
        self.job_name = job_name

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Jobs).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetAll(self, session):
        return session.query(Jobs).all()
    
    @functionLogger
    def Create(self, session):
        session.add(self)
        session.flush()
        session.refresh(self)
        return self


Base.metadata.create_all(engine)
