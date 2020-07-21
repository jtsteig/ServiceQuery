import urllib.parse


class FilterFactory:

    def __init__(self, filter_key, filter_value):
        self.filter_key = filter_key
        self.filter_value = urllib.parse.unquote(filter_value)

    def AppendFilter(self, service):
        if service.filter_key == 'name':
            return service.FilterByName
        elif service.filter_key == 'job':
            return service.FilterByJobs
        elif service.filter_key == 'city':
            return service.FilterByCity
        elif service.filter_key == 'rating':
            return service.FilterByRating
        else:
            return service
