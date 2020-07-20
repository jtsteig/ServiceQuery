class Service:
    def __init__(
                    self,
                    business_name,
                    business_address,
                    reviews,
                    business_hours,
                    operating_cities,
                    work_types,
                    review_rating=0
    ):
        self.business_hours = business_hours
        self.business_name = business_name
        self.business_address = business_address
        self.reviews = reviews
        self.operating_cities = operating_cities
        self.work_types = work_types
