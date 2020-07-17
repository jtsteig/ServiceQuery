from table.citytable import CityTable
from utils.functionlogger import functionLogger

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Cities(CityTable):
    def __init__(self, service_id, city_name):
        self.service_id = service_id
        self.city_name = city_name

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(CityTable).delete()
        session.flush()

    @classmethod
    @functionLogger
    def GetCitiesForService(self, service_id, session):
        return session.query(
            CityTable
        ).filter(
            CityTable.service_id == service_id
        ).all()

    @functionLogger
    def Create(self, session):
        city = CityTable()
        city.service_id = self.service_id
        city.city_name = self.city_name
        session.add(city)
        session.flush()
        session.refresh(city)
        return city
