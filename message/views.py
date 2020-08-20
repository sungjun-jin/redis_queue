import logging
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .redis import RedisQueue
from .exceptions import CustomException

logger = logging.getLogger(__name__)


@api_view(['POST'])
def test(request):
    data = json.loads(request.body)
    key = data['key']
    value = data['value']
    redis = RedisQueue()
    redis.enqueue(key,value)
    response = redis.dequeue(key)
    return Response({"data": response}, status=HTTP_200_OK)
