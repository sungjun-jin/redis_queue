import logging
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .redis import RedisQueue

logger = logging.getLogger(__name__)


@api_view(['POST'])
def post_data(request):
    try:
        # args (key, value)
        data = json.loads(request.body)
        redis = RedisQueue()
        redis.enqueue(data['key'], data['value'])
        return Response(status=HTTP_200_OK)

    except Exception as e:
        return Response({"message": str(e)}, status=400)


