import test_utils
import unittest
import json


class UserIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        test_utils.make_delete_all_request('service')

        body = [{
            "businessName": "Sample Business #1",
            "businessHours": [{
                    "dayOfWeek": "Monday",
                    "open": 9,
                    "close": 5
                }, {
                    "dayOfWeek": "Tuesday",
                    "open": 9,
                    "close": 5
                }, {
                    "dayOfWeek": "Wednesday",
                    "open": 9,
                    "close": 5
                }, {
                    "dayOfWeek": "Thursday",
                    "open": 9,
                    "close": 5
                }, {
                    "dayOfWeek": "Friday",
                    "open": 9,
                    "close": 5
                }],
            "businessAddress": {
                "addressLine1": "1234 Fake St",
                "addressLine2": "Suite 500",
                "city": "Denver",
                "stateAbbr": "CO",
                "postal": "80210"
            },
            "operatingCities": [
                "Denver",
                "Lakewood",
                "Thornton",
                "Golden",
                "Arvada",
                "Centennial",
                "Parker"
            ],
            "workTypes": ["Maid Service", "House Cleaning", "Moving Services"],
            "reviews": [{
                "ratingScore": 4.5,
                "customerComment":
                "Use them weekly to clean our home. Do a great job every time"
            }, {
                "ratingScore": 4,
                "customerComment": "Helped us move homes, very timely"
            }, {
                "ratingScore": 4,
                "customerComment": "On time, did a good job"
            }]
        }, {
            "businessName": "Sample Business #2",
            "businessHours": [{
                "dayOfWeek": "Monday",
                "open": 10,
                "close": 7
            }, {
                "dayOfWeek": "Tuesday",
                "open": 9,
                "close": 7
            }, {
                "dayOfWeek": "Wednesday",
                "open": 10,
                "close": 7
            }, {
                "dayOfWeek": "Thursday",
                "open": 9,
                "close": 7
            }, {
                "dayOfWeek": "Friday",
                "open": 10,
                "close": 7
            }, {
                "dayOfWeek": "Saturday",
                "open": 9,
                "close": 12
            }],
            "businessAddress": {
                "addressLine1": "1234 Foobar St",
                "city": "Denver",
                "stateAbbr": "CO",
                "postal": "80201"
            },
            "operatingCities": [
                "Denver",
                "Thornton",
                "Golden",
                "Arvada",
                "Centennial",
                "Parker"
            ],
            "workTypes": [
                "Maid Service",
                "House Cleaning",
                "Moving Services",
                "Packing"
            ],
            "reviews": [{
                "ratingScore": 4,
                "customerComment": "Move out cleaning"
            }, {
                "ratingScore": 2,
                "customerComment":
                "Broke our dishes because they didn't pack right"
            }, {
                "ratingScore": 5
            }]
        }, {
            "businessName": "Sample Business #3",
            "businessHours": [{
                "dayOfWeek": "Monday",
                "open": 8,
                "close": 6
            }, {
                "dayOfWeek": "Tuesday",
                "open": 8,
                "close": 6
            }, {
                "dayOfWeek": "Wednesday",
                "open": 8,
                "close": 6
            }, {
                "dayOfWeek": "Thursday",
                "open": 8,
                "close": 6
            }, {
                "dayOfWeek": "Friday",
                "open": 8,
                "close": 6
            }, {
                "dayOfWeek": "Saturday",
                "open": 8,
                "close": 6
            }],
            "businessAddress": {
                "addressLine1": "23456 5th Ave",
                "addressLine2": "Suite A",
                "city": "Henderson",
                "stateAbbr": "CO",
                "postal": "80640"
            },
            "operatingCities": [
                "Denver",
                "Commerce City",
                "Thornton",
                "Henderson",
                "Northglenn"
            ],
            "workTypes": ["Packing", "Moving Services"],
            "reviews": [{
                "ratingScore": 5,
                "customerComment":
                "Helped us move across the country, they're great!"
            }]
        }]

        resp = test_utils.make_post_request('service', '', body)
        respJson = resp.json()
        respBody = json.loads(respJson.get('body'))
        self.service_id = respBody[0].get('id')

    @classmethod
    def tearDownClass(self):
        test_utils.make_delete_all_request('service')

    def test_get_all_services(self):
        resp = test_utils.make_get_request('service', '')
        respJson = resp.json()
        self.assertEqual(respJson.get('statusCode'), 200)
        respBody = respJson.get('body')

        self.assertEqual(len(respBody), 3)

    def test_get_one_service(self):
        resp = test_utils.make_get_request('service', self.service_id)
        respJson = resp.json()
        self.assertEqual(respJson.get('statusCode'), 200)
        respBody = respJson.get('body')

        self.assertEqual(respBody.get('businessName'), 'Sample Business #1')
