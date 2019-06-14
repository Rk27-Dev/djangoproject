from django.db import models

# Create your models here.
class contactinfo(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    address=models.CharField(max_length=120)

class student(contactinfo):
    rollno=models.IntegerField()
    marks=models.IntegerField()
class teacher(contactinfo):
    subject=models.CharField(max_length=100)
    sal=models.FloatField()

class contactinfo2(models.Model):
    name=models.CharField(max_length=120)
    email=models.EmailField()
    address=models.CharField(max_length=120)
    class Meta:
        abstract=True
class student2(contactinfo2):
    rollno=models.IntegerField()
    marks=models.IntegerField()
class teacher2(contactinfo2):
    subject=models.CharField(max_length=100)
    sal=models.FloatField()
class parent(models.Model):
    fd1=models.CharField(max_length=120)
    fs2=models.CharField(max_length=120)
class child(parent):
    fd3=models.CharField(max_length=120)
    fd4=models.CharField(max_length=120)
class subchild(child):
    fd5=models.CharField(max_length=120)



# custom manager objects
class custommanager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
class custommanager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('-sal')

class emp(models.Model):
    name=models.CharField(max_length=120)
    sal=models.FloatField()
    email=models.EmailField()
    address=models.CharField(max_length=120)
    objects=custommanager1()
class proxy_emp(emp):
    objects = custommanager2()
    class Meta:
        proxy=True

