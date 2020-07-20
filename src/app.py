from lambdarest import lambda_handler

from service.db_base import Base, Session, engine
from utils.functionlogger import functionLogger
from utils.filterFactory import FilterFactory
from service.serviceservice import ServicesService
from schema.serviceschema import ServiceSchema

import json
import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)

serviceSchema = ServiceSchema()


@functionLogger
def getOffset(event):
    if event.get('queryStringParameters') is not None:
        if 'offset' in event['queryStringParameters']:
            return event['queryStringParameters']['offset']
    return 0


@functionLogger
def getLimit(event):
    if event.get('queryStringParameters') is not None:
        if 'limit' in event['queryStringParameters']:
            return event['queryStringParameters']['limit']
    return 1000000


@functionLogger
def applyFiltersOnQueries(event, service):
    if event.get('queryStringParameters') is not None:
        for parameter, value in event['queryStringParameters'].items():
            filterFactory = FilterFactory(parameter, value)
            service = filterFactory.AppendFilter(service)

    return service


@functionLogger
def getSortArgs(event):
    sortBy = None
    descending = False
    if event.get('queryStringParameters') is not None:
        sortVal = event.get('queryStringParameters').get('sort_by')
        if sortVal is not None:
            sortArgs = sortVal.split('|')
            descending = len(sortArgs) > 1 and sortArgs[1] == 'desc'
            sortBy = sortArgs[0]
    return sortBy, descending


@lambda_handler.handle("get", path="/service")
@functionLogger
def handleGetAllServices(event):
    session = Session()
    sort_by, descending = getSortArgs(event)
    try:
        services = ServicesService(
            session
        ).ApplySorting(
            sort_by, descending
        ).Results(
            getLimit(event),
            getOffset(event)
        )
        results = [json.loads(serviceSchema.dumps(i)) for i in services]
        session.commit()
        return {
            'statusCode': 200,
            'body': results
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': traceback.format_exc()
        }


@lambda_handler.handle("get", path="/service/filter")
@functionLogger
def handleFilterServices(event):
    session = Session()
    sort_by, descending = getSortArgs(event)
    try:
        session = Session()
        service = ServicesService(session)
        filteredServices = applyFiltersOnQueries(
            event,
            service
        ).ApplySorting(
            sort_by, descending
        ).Results(
            getLimit(event),
            getOffset(event)
        )
        results = [
            json.loads(
                serviceSchema.dumps(i)) for i in filteredServices
        ]
        return {
            'statusCode': 200,
            'body': results
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': traceback.format_exc()
        }


@lambda_handler.handle("get", path="/service/<int:id>")
@functionLogger
def handleGetById(event, id):
    try:
        session = Session()
        service = ServicesService(
            session
        ).FilterById(
            id
        ).Results(
            offset=0,
            limit=1)

        session.commit()
        if service is None:
            return {
                'statusCode': 404
            }

        return {
            'statusCode': 200,
            'body': json.loads(serviceSchema.dumps(service))
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': traceback.format_exc()
        }


@lambda_handler.handle("post", path="/service")
@functionLogger
def handleCreateService(event):
    try:
        session = Session()
        services = json.loads(event['body'])
        schema = ServiceSchema(many=True)
        results = []
        for service in schema.load(services):
            servicesService = ServicesService(session)
            results.append(servicesService.Create(
                service
            ))
            session.commit()

        return {
            'statusCode': 200,
            'body': schema.dumps(results)
        }
    except json.decoder.JSONDecodeError as jsonErr:
        return {
            'statusCode': 400,
            'body': 'Invalid json: {}'.format(jsonErr)
        }
    except Exception as err:
        return {
            'statusCode': 400,
            'body': 'Error creating service: {}'.format(err)
        }


@lambda_handler.handle("delete", path="/service/all")
@functionLogger
def handleDeleteAll(event):
    try:
        session = Session()
        ServicesService.DeleteAll(session)
        session.commit()
        return {
            'statusCode': 200
        }
    except Exception as err:
        return {
            'statusCode': 500,
            'body': 'Error deleting all: {}'.format(err)
        }


Base.metadata.create_all(engine)
