from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^uploaditem/', upload_sale, name='upload'),
    url(r'^display/', display_self, name='shelf'),
    url(r'^item/(\d+)', display_product, name='product'),
    url(r'^addcart/(\d+)', add_to_cart, name='addToCart'),
    url(r'^reviewitem/(\d+)', review_item, name='reviewit'),
    url(r'^search/', search_shop, name='searchshop'),
]