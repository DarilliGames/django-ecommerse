from django.db import models

# Create your models here.
class user_profile(models.Model):
    user_id = models.ForeignKey('auth.User')
    following = []
    profile_picture = models.ImageField(upload_to="images", blank=True, null=True)
    