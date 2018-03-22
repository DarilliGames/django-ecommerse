from django.db import models
from django.utils import timezone


class SellItem(models.Model):
    """
    Here we'll define our Post model
    """

    # seller is linked to a registered
    # user in the 'auth_user' table.
    seller = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    max_buy = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
    rating = models.IntegerField()
    reviews = models.IntegerField()


    @property
    def average_rating(self):
        return self.rating / self.reviews

    def __str__(self):
        return self.title
        
