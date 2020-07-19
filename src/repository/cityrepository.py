from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from repository.servicerepository import Services

from utils.functionlogger import functionLogger

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Cities(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    city_name = Column(String, nullable=False)

    def __init__(self, session):
        self.session = session

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Cities).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetCitiesForService(self, service_id, session):
        return session.query(
            Cities
        ).filter(
            Cities.service_id == service_id
        )

    @functionLogger
    def Create(self, service_id, city_name):
        self.service_id = service_id
        self.city_name = city_name
        self.session.add(self)
        self.session.flush()
        self.session.refresh(self)
        return self

    def __str__(self):
        return self.city_name

    def __repr__(self):
        return self.city_name


Base.metadata.create_all(engine)
