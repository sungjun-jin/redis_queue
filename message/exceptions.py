from rest_framework.response import Response
from rest_framework.exceptions import APIException


class CustomException(Exception):

    def __str__(self):
        return "Custom_Exception_Error_Message"


class EnqueueException(Exception):

    def __str__(self):
        return "Redis_Enqueue_Exception"


class DequeueException(Exception):

    def __str__(self):
        return "Redis_Dequeue_Exception"
