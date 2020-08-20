from rest_framework.response import Response
from rest_framework.exceptions import APIException


class CustomException(Exception):

    def __str__(self):
        return "Custom_Exception_Error_Message"



