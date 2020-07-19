from utils.functionlogger import functionLogger

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from service.db_base import Base, engine


class Services(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    business_name = Column(String, nullable=False)
    review_rating = Column(Integer, nullable=False)
    hash_value = Column(String, nullable=False)

    jobs = relationship("Jobs", backref="services")
    reviews = relationship("Reviews", backref="services")
    cities = relationship("Cities", backref="services")
    hours = relationship("Hours", backref="services")
    address = relationship("Addresses", backref="services")

    def __init__(
                    self,
                    review_rating,
                    session
    ):
        self.query = session.query(Services)
        self.review_rating = review_rating
        self.session = session

    @functionLogger
    def FilterById(self, service_id):
        self.query.filter_by(id=service_id)
        return self

    @functionLogger
    def Create(self, session):
        session.add(self)
        session.flush()
        session.refresh(self)
        return self

    @functionLogger
    def FilterByName(self, name):
        self.query = self.query\
            .filter(Services.name == name)
        return self

    @functionLogger
    def FilterByJobs(self, job):
        self.query = self.query\
            .join(Services.jobs, aliased=True)\
            .filter_by(job_name=job)
        return self

    @functionLogger
    def FilterByCity(self, city):
        self.query = self.query\
            .join(Services.cities, aliased=True)\
            .filter_by(city_name=city)
        return self

    @functionLogger
    def FilterByRating(self, rating):
        self.query = self.query\
            .filter(self.review_rating >= rating)
        return self

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        session.query(Services).delete()
        session.flush()

    @functionLogger
    def SortByName(self, descending):
        if descending:
            self.query = self.query\
                .order_by(self.name.desc())
        else:
            self.query = self.query\
                .order_by(self.name)
        return self

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
    def HashValueExists(self, hash_value, session):
        existingHash = session.query(
            Services
        ).filter_by(hash_value=hash_value).all()
        if len(existingHash) > 0:
            return True

        return False

    @functionLogger
    def Results(self, limit, offset):
        return self.query\
            .limit(limit)\
            .offset(offset)\
            .all()


Base.metadata.create_all(engine)
