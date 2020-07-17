from utils.functionlogger import functionLogger
from table.addresstable import AddressTable

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Addresses():
    def __init__(
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
        self.state_abbreviaiton = state_abbreviation
        self.postal = postal

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(AddressTable).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetAddressForService(self, service_id, session):
        return session.query(
            AddressTable
        ).filter(
            AddressTable.service_id == service_id
        ).all()

    @functionLogger
    def Create(self, session):
        address = AddressTable()
        address.service_id = self.service_id
        address.address_line_1 = self.address_line_1
        address.address_line_2 = self.address_line_2
        address.city = self.city
        address.state_abbreviation = self.state_abbreviation
        address.postal = self.postal

        session.add(address)
        session.flush()
        session.refresh(address)
        return address
