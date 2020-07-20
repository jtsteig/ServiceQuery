from marshmallow import Schema, fields, post_load, validate
from model.servicemodel import Service
from model.businesshoursmodel import BusinessHours
from model.businessaddressmodel import BusinessAddress
from model.reviewmodel import Review


class BusinessHoursSchema(Schema):
    day_of_week = fields.Str(data_key="dayOfWeek", validate=validate.OneOf([
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]),
        required=True)
    open_at = fields.Int(data_key="open", required=True)
    close_at = fields.Int(data_key="close", required=True)

    @post_load
    def MakeBusinessHours(self, data, **kwargs):
        return BusinessHours(**data)


class BusinessAddressSchema(Schema):
    address_line_1 = fields.Str(data_key="addressLine1", required=True)
    address_line_2 = fields.Str(data_key="addressLine2", required=False)
    city = fields.Str(required=True)
    state_abbreviation = fields.Str(data_key="stateAbbr", required=True)
    postal = fields.Str(required=True)

    @post_load
    def MakeBusinessAddress(self, data, **kwargs):
        return BusinessAddress(**data)


class ReviewSchema(Schema):
    rating_score = fields.Int(data_key="ratingScore", required=True)
    customer_comment = fields.Str(data_key="customerComment", required=False)

    @post_load
    def MakeReview(self, data, **kwargs):
        return Review(**data)


class ServiceSchema(Schema):
    id = fields.Str(required=False)
    business_name = fields.Str(data_key="businessName", required=True)
    review_rating = fields.Decimal(required=False)
    business_hours = fields.List(
                       fields.Nested(BusinessHoursSchema),
                       data_key="businessHours",
                       required=True
                   )
    business_address = fields.Nested(
        BusinessAddressSchema,
        data_key="businessAddress",
        required=True
    )
    operating_cities = fields.List(
        fields.String(),
        data_key="operatingCities",
        required=True
    )
    work_types = fields.List(
        fields.String(),
        data_key="workTypes",
        required=True
    )
    reviews = fields.List(fields.Nested(ReviewSchema, required=True))

    @post_load
    def makeService(self, data, **kwargs):
        return Service(**data)
