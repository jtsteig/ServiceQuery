import hashlib

from schema.serviceschema import ServiceSchema
from repository.servicerepository import Services
from repository.reviewrepository import Reviews
from repository.addressrepository import Addresses
from repository.jobrepository import Jobs
from repository.hourrepository import Hours
from repository.cityrepository import Cities
from utils.functionlogger import functionLogger
from model.servicemodel import Service


class ServicesService:
    def __init__(self, session):
        self.serviceRepo = Services(session)
        self.session = session

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        Services.DeleteAll(session)

    @functionLogger
    def FilterByName(self, name):
        self.serviceRepo = self.serviceRepo.FilterByName(name)
        return self

    @functionLogger
    def FilterByJobs(self, job):
        self.serviceRepo = self.serviceRepo.FilterByJobs(job)
        return self

    @functionLogger
    def FilterByCity(self, city):
        self.serviceRepo = self.serviceRepo.FilterByCity(city)
        return self

    @functionLogger
    def FilterByRating(self, rating):
        self.serviceRepo = self.serviceRepo.FilterByRating(rating)
        return self

    @functionLogger
    def FilterById(self, service_id, session):
        self.serviceRepo = self.serviceRepo.FilterById(service_id)
        return self

    @functionLogger
    def Results(self, limit, offset):
        results = self.serviceRepo.Results(
            limit,
            offset
        )
        ret = []
        for result in results:
            ret.append(self.GetModelForService(result))
        return ret

    @functionLogger
    def GetModelForService(self, service):
        return Service(
            business_name=service.business_name,
            business_address=service.address,
            reviews=service.reviews,
            business_hours=service.hours,
            operating_cities=service.cities,
            work_types=service.jobs
        )

    @functionLogger
    def Create(
            self,
            createService
    ):
        service_schema = ServiceSchema()
        hash_value = hashlib.md5(
            service_schema.dumps(
                createService
            ).encode()
        ).hexdigest()

        if Services.HashValueExists(hash_value, self.session):
            return

        review_rating = sum(
            review.rating_score for review in createService.reviews
        ) / len(createService.reviews)

        service = Services(review_rating, self.session)

        for city in createService.operating_cities:
            cityRepo = Cities(city.city_name)
            service.cities.append(cityRepo)

        for review in createService.reviews:
            reviewRepo = Reviews(
                rating_score=review.rating_score,
                customer_comment=review.customer_comment
            )
            service.reviews.append(reviewRepo)

        for job in createService.work_types:
            jobRepo = Jobs(
                rating_score=review.rating_score,
                customer_comment=review.customer_comment
            )
            service.jobs.append(jobRepo)

        for hours in createService.business_hours:
            hourRepo = Hours(
                day_of_week=hours.day_of_week,
                open_at=hours.open_at,
                close_at=hours.close_at
            )
            service.hours.append(hourRepo)

        addressRepo = Addresses(
            address_line_1=createService.business_address.address_line_1,
            address_line_2=createService.business_address.address_line_2,
            city=createService.business_address.city,
            state_abbreviation=createService.business_address
            .state_abbreviation,
            postal=createService.business_address.postal
        )
        service.address.append(addressRepo)

        service.Create(self.session)

        return self.GetModelForService(service, self.session)
