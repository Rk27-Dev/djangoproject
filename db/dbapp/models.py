from django.db import models

# Create your models here.
class dbmodel(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    sal=models.FloatField()