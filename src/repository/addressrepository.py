from utils.functionlogger import functionLogger
from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from repository.servicerepository import Services

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Addresses(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    address_line_1 = Column(String, nullable=False)
    address_line_2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state_abbreviation = Column(String, nullable=False)
    postal = Column(String, nullable=False)

    def __init__(
        self,
        session
    ):
        self.session = session

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Addresses).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetAddressForService(self, service_id, session):
        return session.query(
            Addresses
        ).filter(
            Addresses.service_id == service_id
        ).first()

    @functionLogger
    def Create(
        self,
        service_id,
        address_line_1,
        address_line_2,
        city,
        state_abbreviation,
        postal
    ):
        self.service_id = service_id
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state_abbreviation = state_abbreviation
        self.postal = postal
        self.session.add(self)
        self.session.flush()
        self.session.refresh(self)
        return self


Base.metadata.create_all(engine)
