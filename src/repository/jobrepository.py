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

    def __init__(self, job_name):
        self.job_name = job_name

    def __repr__(self):
        return self.job_name

    def __str__(self):
        return self.job_name


Base.metadata.create_all(engine)
