from repository.servicerepository import Services
from utils.functionlogger import functionLogger


class ServicesService:
    @classmethod
    @functionLogger
    def GetAll(self, session):
        return Services.InitQuery(session).Results()

    def InitQuery(self, session):
        self.query = Services.InitQuery(session)

    def DeleteAll(self, session):
        Services.DeleteAll(session)

    def FilterByName(self, name):
        return self.query.FilterByName(name)

    def FilterByJobs(self, job):
        return self.query.FilterByJobs(job)

    def FilterByCity(self, city):
        return self.query.FilterByCity(city)

    def FilterByRating(self, rating):
        return self.query.FilterByRating(rating)

    def GetOne(self, service_id):
        return self.query.GetOne(service_id)

    def Results(self):
        return self.query.Results()

    def Create(self, service):
        service = Services(
            service.name,
            service.review_rating,
            service.open_time,
            service.close_time,
            service.address_line_1,
            service.address_line_2,
            service.city,
            service.state_abbreviation,
            service.postal
        )
        return service.Create()
