from utils.functionlogger import functionLogger
from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from table.servicetable import ServiceTable
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Jobs(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(ServiceTable.id), nullable=False)
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
    def GetJobForService(self, service_id, session):
        return session.query(
            Jobs
        ).filter(
            Jobs.service_id == service_id
        )

    @functionLogger
    def Create(self, session):
        job = Jobs()
        job.service_id = self.service_id
        job.job_name = self.job_name
        session.add(job)
        session.flush()
        session.refresh(job)
        return job


Base.metadata.create_all(engine)
