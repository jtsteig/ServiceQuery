from repository.servicerepository import Services
from repository.reviewrepository import Reviews
from repository.addressrepository import Addresses
from repository.jobrepository import Jobs
from repository.hourrepository import Hours
from repository.cityrepository import Cities
from utils.functionlogger import functionLogger
from model.servicemodel import Service


class ServicesService:
    @classmethod
    @functionLogger
    def InitQuery(self, session):
        self.query = Services.InitQuery(session)
        return self

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        Services.DeleteAll(session)

    @classmethod
    @functionLogger
    def FilterByName(self, name):
        self.query = self.query.FilterByName(name)
        return self

    @classmethod
    @functionLogger
    def FilterByJobs(self, job):
        self.query = self.query.FilterByJobs(job)
        return self

    @classmethod
    @functionLogger
    def FilterByCity(self, city):
        self.query = self.query.FilterByCity(city)
        return self

    @classmethod
    @functionLogger
    def FilterByRating(self, rating):
        self.query = self.query.FilterByRating(rating)
        return self

    @classmethod
    @functionLogger
    def FilterById(self, service_id, session):
        self.query = self.query.FilterById(service_id)
        return self

    @classmethod
    @functionLogger
    def Results(self, session):
        results = self.query.Results()
        ret = []
        for result in results:
            ret.append(self.GetModelForService(result, session))
        return ret

    @classmethod
    @functionLogger
    def GetReviewsForService(
        self,
        service_id,
        session
    ):
        return Reviews.GetReviewsForService(service_id, session)

    @classmethod
    @functionLogger
    def GetAddressForService(
        self,
        service_id,
        session
    ):
        return Addresses.GetAddressForService(service_id, session)

    @classmethod
    @functionLogger
    def GetJobsForService(
        self,
        service_id,
        session
    ):
        return Jobs.GetJobsForService(service_id, session)

    @classmethod
    @functionLogger
    def GetHoursForService(
        self,
        service_id,
        session
    ):
        return Hours.GetHoursForService(service_id, session)

    @classmethod
    @functionLogger
    def GetCitiesForService(
        self,
        service_id,
        session
    ):
        return Cities.GetCitiesForService(service_id, session)

    @classmethod
    @functionLogger
    def GetModelForService(self, service, session):
        return Service(
            business_name=service.business_name,
            business_address=self.GetAddressForService(service.id, session),
            reviews=self.GetReviewsForService(service.id, session),
            business_hours=self.GetHoursForService(service.id, session),
            operating_cities=self.GetCitiesForService(service.id, session),
            work_types=self.GetJobsForService(service.id, session)
        )

    @classmethod
    @functionLogger
    def Create(
            self,
            createService,
            session
    ):
        review_rating = sum(
            review.rating_score for review in createService.reviews
        ) / len(createService.reviews)

        serviceRepo = Services(
            business_name=createService.business_name,
            review_rating=review_rating,
        )
        service = serviceRepo.Create(session)
        return self.GetModelForService(service, session)
