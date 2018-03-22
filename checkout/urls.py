from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
    url(r'^process/', process, name='process'),
]