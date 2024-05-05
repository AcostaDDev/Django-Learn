import json
import logging
from typing import Callable


class LoggingMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.request_logger = logging.getLogger('middleware.request')
        self.response_logger = logging.getLogger('middleware.response')

    def __call__(self, request):
        self.request_logger.info('request recived', extra={
            'user': json.dumps({
                'id': request.user.id,
                'username': request.user.username
            }),
            'path': request.path,
            'body': json.dumps(request.POST)
        })

        response = self.get_response(request)

        self.response_logger.info('response recived', extra={
            'user': json.dumps({
                'id': request.user.id,
                'username': request.user.username
            }),
            'path': request.path,
            'status': response.status_code,
            'body': json.dumps(response.__dict__.get('data', {}))       # data, {} --> si no hay data, retorna un diccionario vacio
        })

        return response
