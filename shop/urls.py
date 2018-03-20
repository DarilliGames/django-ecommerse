from django.conf.urls import url, include
from .views import *


urlpatterns = [
    url(r'^uploaditem/', upload_sale, name='upload'),
    url(r'^display/', display_self, name='shelf'),
    url(r'^item/(\d+)', display_product, name='product'),
   
]