from django.db import models
from django.contrib.auth.models import  User
from django.utils import timezone
from django.urls import reverse
# from django.core.urlresolvers import reverse
# Create your models here.

class customanager(models.Manager):
    def get_queryset(self):
        return  super().get_queryset().filter(status='published')
class Post(models.Model):
    STATUS_CHOICES=(('draft','DRAFT'),('published','PUBLISHED'))
    tittle=models.CharField(max_length=256)
    slug=models.SlugField(max_length=256,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.PROTECT)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft')
    objects=customanager()
    class Meta:
        ordering=('-publish',)


    def __str__(self):
        return  self.tittle
    #
    # def get_absolute_url(self):
    #     return  reverse('post_details',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

    #
    def get_absolute_url(self):
        return  reverse('post_details',args=[self.publish.year,self.publish.strftime("%m"),self.publish.strftime("%d"),self.slug])
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.PROTECT)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('-created',)
    def __str__(self):
        return 'commented by{} on {}'.format(self.name,self.post)
