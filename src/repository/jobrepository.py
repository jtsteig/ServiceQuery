from utils.functionlogger import functionLogger
from table.jobtable import JobTable

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Jobs():
    def __init__(self, service_id, job_name):
        self.service_id = service_id
        self.job_name = job_name

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(JobTable).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetAll(self, session):
        return session.query(JobTable).all()

    @functionLogger
    def Create(self, session):
        job = JobTable()
        job.service_id = self.service_id
        job.job_name = self.job_name
        session.add(job)
        session.flush()
        session.refresh(job)
        return job
