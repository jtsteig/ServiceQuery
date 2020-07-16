from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from table.servicetable import ServiceTable


class CityTable(Base):
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(ServiceTable.id), nullable=False)
    city_name = Column(String, nullable=False)


Base.metadata.create_all(engine)
