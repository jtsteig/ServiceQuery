import datetime
import re


# This is a series of static functions which validate shared fields
class Validations:

    @staticmethod
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('Email cannot be blank')
        validEmailRegex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(validEmailRegex, email):
            raise AssertionError('Invalid email address')
        return email

    @staticmethod
    def validate_name(self, key, name):
        if not name:
            raise AssertionError('Name cannot be blank')
        if not len(name) >= 2:
            raise AssertionError('Name has to be at least two letters')
        return name

    @staticmethod
    def validate_service_hour(self, key, hour):
        if (hour < 0) or (hour > 24):
            raise AssertionError('Hours must be between 0 and 24, and in UTC')
        return hour

    @staticmethod
    def validate_review_rating(self, key, rating):
        if (rating < 0) or (rating > 5):
            raise AssertionError('Rating must be between 0 and 5')
        return rating

    @staticmethod
    def validate_date(self, key, date):
        try:
            datetime.datetime(date.year, date.month, date.day)
            return date
        except ValueError:
            raise AssertionError('Invalid date time.')

    @staticmethod
    def validate_dayOfWeek(self, key, dayOfWeek):
        daysOfWeek = [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday"
                ]
        if dayOfWeek in daysOfWeek:
            return dayOfWeek
        raise AssertionError('Invalid day of week')
