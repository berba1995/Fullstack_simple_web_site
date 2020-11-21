from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


 # définition  d'un modèle utilisateur personnalisé permettant d'utiliser l'email pour se connecter
class CustomUser(AbstractUser):


    email = models.EmailField(_('email address'), unique=True,
     error_messages={
            'unique': _("A user with that username already exists."),
        })
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'first_name', 'last_name' ]
    username = models.CharField(
        max_length=150,
        blank=True,
    )



class UserProfileInfo(models.Model):
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #portfolio_site = models.URLField(blank=True)
    photo_profil = models.ImageField(upload_to='photo_profil',blank=True)
    def __str__(self):
      return self.user.username
# Create your models here.
