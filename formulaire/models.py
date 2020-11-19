from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    #portfolio_site = models.URLField(blank=True)
    photo_profil = models.ImageField(upload_to='photo_profil',blank=True)
    def __str__(self):
      return self.user.username
# Create your models here.
