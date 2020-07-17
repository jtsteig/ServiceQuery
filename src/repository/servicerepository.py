from utils.functionlogger import functionLogger
from table.citytable import CityTable
from table.servicetable import ServiceTable

from repository.jobrepository import Jobs


class Services():
    def __init__(
                    self,
                    business_name,
                    review_rating,
                ):
        self.service = ServiceTable()
        self.service.business_name = business_name
        self.service.review_rating = review_rating
        self.query = None

    @classmethod
    @functionLogger
    def InitQuery(self, session):
        self.query = session.query(ServiceTable)
        return self

    @classmethod
    @functionLogger
    def FilterById(self, service_id):
        self.query.filter_by(id=service_id)
        return self

    @functionLogger
    def Create(self, session):
        session.add(self.service)
        session.flush()
        session.refresh(self.service)
        return self.service

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
                Jobs,
                Jobs.service_id == self.id,
                full=True
            )\
            .filter(
                Jobs.job_name == job
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
