from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from table.servicetable import ServiceTable
from utils.functionlogger import functionLogger

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(ServiceTable.id), nullable=False)
    customer_comment = Column(String, nullable=False)
    rating_score = Column(Integer, nullable=False)

    def __init__(self, service_id, customer_comment, rating_score):
        self.service_id = service_id
        self.customer_comment = customer_comment
        self.rating_score = rating_score

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Reviews).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetReviewsForService(self, service_id, session, offset=0, limit=10):
        return session.query(Reviews)\
            .filter(Reviews.service_id == service_id)\
            .limit(limit)\
            .offset(offset)\
            .all()

    @functionLogger
    def Create(self, session):
        session.add(self)
        session.flush()
        session.refresh(self)
        return self


Base.metadata.create_all(engine)
