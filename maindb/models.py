from django.db import models

# Create your models here.

class testdn(models.Model):
    username = models.CharField(max_length=50)
    age = models.IntegerField()