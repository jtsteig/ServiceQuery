import os
import requests

headers = {'Content-type': 'application/json'}


def get_host_uri(classType):
    value = os.environ["api_host"]
    return 'https://{}/dev/{}'.format(value, classType)


def add_parameters(uri, parameterValue):
    if(parameterValue):
        uri = '{}/{}'.format(uri, parameterValue)
    return uri


def get_request_uri(classType, parameterValue):
    uri = get_host_uri(classType)
    return add_parameters(uri, parameterValue)


def make_get_request(classType, parameterValue):
    req = get_request_uri(classType, parameterValue)
    return requests.get(req, headers=headers)


def make_patch_request(classType, parameterValue, body):
    req = get_request_uri(classType, parameterValue)
    return requests.patch(req, data=body, headers=headers)


def make_delete_request(classType, parameterValue):
    req = get_request_uri(classType, parameterValue)
    return requests.delete(req, headers=headers)


def make_post_request(classType, parameterValue, body):
    req = get_request_uri(classType, parameterValue)
    return requests.post(req, json=body, headers=headers)


def make_delete_all_request(classType):
    req = get_host_uri(classType) + "/all"
    return requests.delete(req, headers=headers)
