from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^submit/', submit_review, name='submitreview'),
]