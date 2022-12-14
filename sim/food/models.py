from audioop import reverse
from distutils.command.upload import upload
from email.mime import image
from operator import length_hint
from pickle import TRUE
from pydoc import describe
from pyexpat import model
from turtle import left
from django.db import models
from django.urls import reverse
from food.fields import ThumbnailImageField

# Create your models here.
class zip(models.Model):
    name = models.CharField('',max_length=30)
    description = models.CharField('One Line Description' , max_length=100, blank=True)
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='OWNER', blank=True,null=True)


    class Meta:
        ordering= ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food:zip_detail', args= (self.id,))

class food(models.Model):
    zip = models.ForeignKey(zip, on_delete=models.CASCADE)
    title = models.CharField('TITLE',max_length=30)
    description =models.TextField('food describe', blank=True)
    image = ThumbnailImageField(upload_to = 'food/%Y%m')
    upload_dt = models.DateField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='OWNER', blank=True,null=True)
    lat = models.FloatField('latitude', blank=True,null=True)
    lng = models.FloatField('longtite', blank=True,null=True)
   
    

    class Meta:
        ordering= ('title',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('food:food_detail', args= (self.id,))

