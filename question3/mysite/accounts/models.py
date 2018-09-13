
from django.contrib.auth.models import PermissionsMixin,User

from django.db import models
from django.utils import timezone


class User(User,PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)