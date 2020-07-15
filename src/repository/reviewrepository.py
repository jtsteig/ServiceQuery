from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from repository.servicerepository import Services
from utils.functionlogger import functionLogger

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    review_comment = Column(String, nullable=False)
    review_rating = Column(Integer, nullable=False)

    def __init__(self, service_id, review_comment, review_rating):
        self.service_id = service_id
        self.review_comment = review_comment
        self.review_rating = review_rating

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Reviews).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetAll(self, session):
        return session.query(Reviews).all()

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
