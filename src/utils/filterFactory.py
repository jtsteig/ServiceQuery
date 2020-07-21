import urllib.parse


class FilterFactory:

    def __init__(self, filter_key, filter_value):
        self.filter_key = filter_key
        self.filter_value = urllib.parse.unquote(filter_value)

    def AppendFilter(self, service):
        if self.filter_key == 'name':
            return service.FilterByName(self.filter_value)
        elif self.filter_key == 'job':
            return service.FilterByJobs(self.filter_value)
        elif self.filter_key == 'city':
            return service.FilterByCity(self.filter_value)
        elif self.filter_key == 'rating':
            return service.FilterByRating(self.filter_value)
        elif self.filter_key == 'weekday':
            return service.FilterByWeekday(self.filter_value)
        else:
            return service
