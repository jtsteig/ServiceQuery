from utils.functionlogger import functionLogger
from table.citytable import CityTable
from table.jobtable import JobTable
from table.servicetable import ServiceTable


class Services(ServiceTable):
    def __init__(
                    self,
                    name,
                    review_rating,
                    open_time,
                    close_time,
                    address_line_1,
                    address_line_2,
                    city,
                    state_abbreviation,
                    postal
                ):
        self.service = ServiceTable()
        self.service.name = name
        self.service.address_line_1 = address_line_1
        self.service.address_line_2 = address_line_2
        self.service.city = city
        self.service.state_abbreviation = state_abbreviation
        self.service.postal = postal

    @classmethod
    @functionLogger
    def InitQuery(self, session):
        self.query = session.query(ServiceTable)

    @classmethod
    @functionLogger
    def GetOne(self, service_id):
        return self.query.filter_by(id=service_id).first()

    @classmethod
    @functionLogger
    def Create(self, session):
        session.add(self.service)
        session.flush()
        session.refresh(self.service)
        return self

    @classmethod
    @functionLogger
    def FilterByName(self, name):
        self.query = self.query\
            .filter(ServiceTable.name.match(name))
        return self

    @classmethod
    @functionLogger
    def FilterByJobs(self, job):
        self.query = self.query\
            .join(
                JobTable,
                JobTable.service_id == self.id,
                full=True
            )\
            .filter(
                JobTable.job_name == job
            )
        return self

    @classmethod
    @functionLogger
    def FilterByCity(self, city):
        self.query = self.query\
            .join(
                CityTable,
                CityTable.service_id == self.id,
                full=True
            )\
            .filter(
                CityTable.city_name == city
            )
        return self

    @classmethod
    @functionLogger
    def FilterByRating(self, rating):
        self.query = self.query\
            .filter(
                    ServiceTable.review_rating >= rating
            )

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(ServiceTable).delete()
        session.flush()

    @classmethod
    @functionLogger
    def SortByName(self, descending=False):
        if descending:
            self.query = self.query\
                .order_by(self.name.desc())
        else:
            self.query = self.query\
                .order_by(self.name)
        return self

    @classmethod
    @functionLogger
    def SortByRating(self, descending=False):
        if descending:
            self.query = self.query\
                .order_by(self.review_rating)
        else:
            self.query = self.query\
                .order_by(self.review_rating.desc())
        return self

    @classmethod
    @functionLogger
    def Results(self, offset=0, limit=10):
        return self.query.offset(offset).limit(limit).all()
