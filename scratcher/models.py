from __future__ import unicode_literals
from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100)
    current_balance = models.FloatField()
    saving_category = models.IntegerField()
    delta = models.FloatField()
# 