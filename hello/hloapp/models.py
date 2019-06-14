from django.db import models

# Create your models here.
class registermodel(models.Model):
    name=models.CharField(max_length=10)
    sal=models.FloatField()
    age=models.IntegerField()
    address=models.CharField(max_length=20)
