from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from service.db_base import Base, engine


class ServiceTable(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    business_name = Column(String, nullable=False)
    review_rating = Column(Integer, nullable=False)
    address_line_1 = Column(String, nullable=False)
    address_line_2 = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state_abbreviation = Column(String, nullable=False)
    postal = Column(String, nullable=False)
    children = relationship('Child')


Base.metadata.create_all(engine)
