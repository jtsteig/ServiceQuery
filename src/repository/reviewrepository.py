from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from utils.functionlogger import functionLogger
from repository.servicerepository import Services

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Reviews(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(Services.id), nullable=False)
    customer_comment = Column(String, nullable=False)
    rating_score = Column(Integer, nullable=False)

    def __init__(self, customer_comment, rating_score):
        self.customer_comment = customer_comment
        self.rating_score = rating_score

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Reviews).delete()
        session.flush()


Base.metadata.create_all(engine)
