
from django.urls import path

from message.views import post_data


urlpatterns = [
    path('post/', post_data),
]
