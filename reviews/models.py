from django.db import models
from shop.models import SellItem

class Review(models.Model):
    author = models.ForeignKey('auth.User')
    item = models.ForeignKey(SellItem, blank=False)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title