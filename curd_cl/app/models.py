from django.db import models
# from django.core.Urlresolvers import  reverse
class companymodel(models.Model):
    name=models.CharField(max_length=20)
    loc=models.CharField(max_length=50)
    ceo=models.CharField(max_length=20)
    def get_absolute_url(self):
        pass


