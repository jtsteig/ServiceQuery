from marshmallow import Schema, fields, post_load, validate
from model.servicemodel import Service


class BusinessHoursSchema(Schema):
    dayOfWeek = fields.Str(validate=validate.OneOf([
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]),
        required=True)
    open_time = fields.Int(data_key="open", required=True)
    close_time = fields.Int(data_key="close", required=True)


class BusinessAddressSchema(Schema):
    address_line_1 = fields.Str(data_key="addressLine1", required=True)
    address_line_2 = fields.Str(data_key="addressLine2", required=False)
    city = fields.Str(required=True)
    state_abbreviation = fields.Str(data_key="stateAbbr", required=True)
    postal = fields.Str(required=True)


class ReviewSchema(Schema):
    ratingScore = fields.Int(required=True)
    customerComment = fields.Str(required=False)


class ServiceSchema(Schema):
    id = fields.Str(required=False)
    businessName = fields.Str(required=True)
    businessHours = fields.List(
                       fields.Nested(BusinessHoursSchema),
                       required=True
                   )
    businessAddress = fields.Nested(BusinessAddressSchema, required=True)
    operatingCities = fields.List(fields.Str, required=True)
    workTypes = fields.List(fields.Str, required=True)
    reviews = fields.Nested(ReviewSchema, required=True)

    @post_load
    def makeService(self, data, **kwargs):
        return Service(**data)
