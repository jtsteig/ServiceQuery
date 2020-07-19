from utils.functionlogger import functionLogger
from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from repository.servicerepository import Services
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    job_name = Column(String, nullable=False)

    def __init__(self, session):
        self.session = session

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Jobs).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetJobForService(self, service_id, session):
        return session.query(
            Jobs
        ).filter(
            Jobs.service_id == service_id
        )

    @functionLogger
    def Create(self, service_id, job_name):
        self.service_id = service_id
        self.job_name = job_name
        self.session.add(self)
        self.session.flush()
        self.session.refresh(self)
        return self

    def __repr__(self):
        return self.job_name

    def __str__(self):
        return self.job_name


Base.metadata.create_all(engine)
