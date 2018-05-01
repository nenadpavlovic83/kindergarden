from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)


class UserProfilePage(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #more models
    portofolio_site = models.URLField(blank=True)

    def __str__(self):
        return self.user.username
