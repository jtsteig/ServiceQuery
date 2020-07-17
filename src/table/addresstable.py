from sqlalchemy import Column, Integer, String, ForeignKey

from service.db_base import Base, engine
from table.servicetable import ServiceTable


class AddressTable(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey(ServiceTable.id), nullable=False)
    address_line_1 = Column(String, nullable=False)
    address_line_2 = Column(String, nullable=True)
    city = Column(String, nullable=False)
    state_abbreviation = Column(String, nullable=False)
    postal = Column(String, nullable=False)


Base.metadata.create_all(engine)
