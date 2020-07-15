from marshmallow import Schema, OneOf, fields, post_load
from models.servicemodel import Service


class BusinessHoursSchema(Schema):
    dayOfWeek = fields.Str(validate=OneOf([
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]),
        required=True)
    open_at = fields.Int(attribute="open", required=True)
    close_at = fields.Int(attribute="close", required=True)


class BusinessAddressSchema(Schema):
    address_line_1 = fields.Str(attribute="addressLine1", required=True)
    address_line_2 = fields.Str(attribute="addressLine2", required=False)
    city = fields.Str(required=True)
    state_abbreviation = fields.Str(attribute="stateAbbr", required=True)
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
