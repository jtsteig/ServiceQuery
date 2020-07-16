from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from service.db_base import Base, engine


class ServiceTable(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    review_rating = Column(Integer, nullable=False)
    open_time = Column(Integer, nullable=False)
    close_time = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    children = relationship('Child')


Base.metadata.create_all(engine)
