
from django.urls import path

from message.views import test


urlpatterns = [
    path('test/', test),
]
