"""
Custom API exceptions.
"""
from rest_framework import status
from rest_framework.exceptions import APIException

import market_simulation.common.constants as constant
from rest_framework import status


class BadRequest(APIException):
    """
    Custom BadRequest exception.
    """
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = constant.INVALID_CONTENT


class NoContentException(APIException):
    """
    Custom No Content exception.
    """
    status_code = status.HTTP_204_NO_CONTENT
    default_detail = constant.NO_CONTENT


class UnProcessableEntity(APIException):
    """
    Custom Unprocessable exception.
    """
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = constant.UNPROCESSABLE


class NotOwner(APIException):
    """
    Custom Unauthrize exception.
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = constant.NOT_OWNER
