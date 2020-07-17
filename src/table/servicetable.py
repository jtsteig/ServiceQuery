from sqlalchemy import Column, String, Integer
from service.db_base import Base, engine


class ServiceTable(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    business_name = Column(String, nullable=False)
    review_rating = Column(Integer, nullable=False)


Base.metadata.create_all(engine)
