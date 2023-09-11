"""
Custom API exceptions.
"""
from rest_framework import status
from rest_framework.exceptions import APIException

import market_simulation.common.constants as constant


class BadRequest(APIException):
    """
    Custom BadRequest exception.
    """
    status_code = 400
    default_detail = constant.INVALID_CONTENT


class NoContentException(APIException):
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = constant.NO_CONTENT


class UnProcessableEntity(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = constant.UNPROCESSABLE


class NotOwner(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = constant.NOT_OWNER
