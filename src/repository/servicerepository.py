from sqlalchemy import Column, String, Integer, DateTime

from utils.functionlogger import functionLogger
from service.db_base import Base, engine
from repository.jobrepository import Jobs
from repository.cityrepository import Cities


class Services(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    review_rating = Column(Integer, nullable=False)
    open_time = Column(DateTime, nullable=False)
    close_time = Column(DateTime, nullable=False)
    address = Column(String, nullable=False)

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
        self.name = name
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state_abbreviation = state_abbreviation
        self.postal = postal

    @classmethod
    @functionLogger
    def InitQuery(self, session):
        self.query = session.query(Services)

    @classmethod
    @functionLogger
    def GetOne(self, service_id):
        return self.query.filter_by(id=service_id).first()

    @classmethod
    @functionLogger
    def Create(self, session):
        session.add(self)
        session.flush()
        session.refresh(self)
        return self

    @classmethod
    @functionLogger
    def FilterByName(self, name):
        self.query = self.query\
            .filter(Services.name.match(name))
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
                Cities,
                Cities.service_id == self.id,
                full=True
            )\
            .filter(
                Cities.city_name == city
            )
        return self

    @classmethod
    @functionLogger
    def FilterByRating(self, rating):
        self.query = self.query\
            .filter(
                    Services.review_rating >= rating
            )

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Services).delete()
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

Base.metadata.create_all(engine)
