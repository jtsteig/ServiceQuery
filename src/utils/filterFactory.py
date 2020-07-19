import urllib.parse


class FilterFactory:

    def __init__(self, filter_key, filter_value):
        self.filter_key = filter_key
        self.filter_value = urllib.parse.unquote(filter_value)

    def AppendFilter(self, service):
        return {
            'name': service.FilterByName,
            'job': service.FilterByJobs,
            'city': service.FilterByCity,
            'rating': service.FilterByRating
        }[self.filter_key](self.filter_value)
