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
        self.serviceRepo = Services(0, '', '', session)
        self.session = session

    @classmethod
    @functionLogger
    def DeleteAll(self, session):
        Reviews.DeleteAll(session)
        Addresses.DeleteAll(session)
        Jobs.DeleteAll(session)
        Hours.DeleteAll(session)
        Cities.DeleteAll(session)
        Services.DeleteAll(session)

    @functionLogger
    def ApplySorting(self, sortBy, descending):
        if sortBy == 'name':
            self.serviceRepo = self.serviceRepo.SortByName(descending)
        if sortBy == 'rating':
            self.serviceRepo = self.serviceRepo.SortByRating(descending)
        return self

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
    def FilterById(self, service_id):
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
    def SingleResult(self):
        result = self.serviceRepo.SingleResult()
        return self.GetModelForService(result)

    @functionLogger
    def GetModelForService(self, service):
        return Service(
            business_name=service.business_name,
            business_address=service.address.first(),
            reviews=service.reviews,
            business_hours=service.hours,
            operating_cities=service.cities,
            work_types=service.jobs,
            review_rating=service.review_rating,
            id=service.id
        )

    @functionLogger
    def Create(
            self,
            createService
    ):
        service_schema = ServiceSchema()
        createService.review_rating = sum(
            review.rating_score for review in createService.reviews
        ) / len(createService.reviews)

        hash_value = hashlib.md5(
            service_schema.dumps(
                createService
            ).encode()
        ).hexdigest()

        if Services.HashValueExists(hash_value, self.session):
            return

        service = Services(
            createService.business_name,
            createService.review_rating,
            hash_value,
            self.session
        )

        for city in createService.operating_cities:
            cityRepo = Cities(city)
            service.cities.append(cityRepo)

        for review in createService.reviews:
            reviewRepo = Reviews(
                rating_score=review.rating_score,
                customer_comment=review.customer_comment
            )
            service.reviews.append(reviewRepo)

        for job in createService.work_types:
            jobRepo = Jobs(job)
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

        return self.GetModelForService(service)
