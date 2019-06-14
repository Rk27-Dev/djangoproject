from django.db import models

# Create your models here.
class restmodel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    sal=models.FloatField()
    ph_no=models.IntegerField()
    email=models.EmailField()