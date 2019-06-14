from django.db import models

# Create your models here.
class registermodel(models.Model):
    name=models.CharField(max_length=20)
    dept=models.CharField(max_length=30)
    sal=models.FloatField()
