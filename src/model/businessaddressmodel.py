class BusinessAddress:
    def __init__(
        self,
        address_line_1,
        city,
        state_abbreviation,
        postal,
        address_line_2=''
    ):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.city = city
        self.state_abbreviation = state_abbreviation
        self.postal = postal
