class Service:
    def __init__(
                    self,
                    name,
                    review_rating,
                    address_line_1,
                    address_line_2,
                    city,
                    state_abbreviation,
                    postal,
                    reviews,
                    cities,
                    jobs
    ):
        self.name = name
        self.review_rating = review_rating
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state_abbreviation = state_abbreviation
        self.postal = postal
        self.reviews = reviews
        self.cities = cities
        self.jobs = jobs
