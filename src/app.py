from lambdarest import lambda_handler

from service.db_base import Base, Session, engine
from utils.functionlogger import functionLogger
from service.serviceservice import ServicesService
from schema.serviceschema import ServiceSchema

import json
import logging
import traceback

logger = logging.getLogger()
logger.setLevel(logging.INFO)

serviceSchema = ServiceSchema()

session = Session()


@lambda_handler.handle("get", path="/service")
@functionLogger
def handleGetAllServices(event):
    try:
        services = ServicesService.GetAll(session)
        results = [json.loads(serviceSchema.dumps(i)) for i in services]
        session.commit()
        return {
            'statusCode': 200,
            'body': results
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': traceback.format_err()
        }


@lambda_handler.handle("get", path="/service/<int:id>")
@functionLogger
def handleGetService(event, id):
    try:
        user = ServicesService.Get(id, session)
        session.commit()
        if user is None:
            return {
                'statusCode': 404
            }

        return {
            'statusCode': 200,
            'body': serviceSchema.dump(user)
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': traceback.format_err()
        }


@lambda_handler.handle("post", path="/service")
@functionLogger
def handleCreateService(event):
    try:
        createService = serviceSchema.loads(event["body"])
        user = ServicesService.Create(createService)
        session.commit()
        return {
            'statusCode': 200,
            'body': serviceSchema.dumps(user)
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
