from django.db import models


# Create your models here.

class Object(models.Model):
    name = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    specifications = models.CharField(max_length=255)
    historik = models.CharField(max_length=255)
    avariem_situation = models.CharField(max_length=255)
