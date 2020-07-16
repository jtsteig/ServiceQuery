import test_utils
import unittest
import json


class UserIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        test_utils.make_delete_all_request('service')

        body = {
                    "businessName:": "Sample Business #3",
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
                }

        resp = test_utils.make_post_request('service', '', body)
        respJson = resp.json()
        print(respJson)
        respBody = json.loads(respJson.get('body'))
        self.user_id = respBody.get('id')

#    @classmethod
#    def tearDownClass(self):
#        test_utils.make_delete_all_request('users')

    def test_get_all_services(self):
        resp = test_utils.make_get_request('service', '')
        respJson = resp.json()
        self.assertEqual(respJson.get('statusCode'), 200)
        respBody = respJson.get('body')

        self.assertEqual(respBody[0].get('email'), 'testCreate2@email.com')
        self.assertEqual(respBody[0].get('name'), 'testname2')

    def test_get_one_user(self):
        resp = test_utils.make_get_request('service', self.user_id)
        respJson = resp.json()
        self.assertEqual(respJson.get('statusCode'), 200)
        respBody = respJson.get('body')

        self.assertEqual(respBody.get('email'), 'testCreate2@email.com')
        self.assertEqual(respBody.get('name'), 'testname2')
