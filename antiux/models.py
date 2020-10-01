import datetime
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    password = models.CharField(max_length=41, null=True, blank=True)

    def __str__(self):
        return self.password
        
    def search_user(cls, password):
        search_results = cls(password=password)
        return search_results