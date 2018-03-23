from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', cart, name='cart'),
    url(r'^addtocart/', add_to_cart, name='add_to_cart'),
    url(r'^removecart/(\d+)/', remove_from_cart, name='removefromcart'),
    url(r'^inccart/(\d+)/', add_count_cart, name='addammount'),
    url(r'^deccart/(\d+)/', dec_count_cart, name='decammount'),
    url(r'^updatecart/(\d+)/', updatecart, name='updatecart'),
    url(r'^dumpcart/', dumpcart, name='emptycart'),
    url(r'^orders/', check_order, name='checkorders'),
    
]