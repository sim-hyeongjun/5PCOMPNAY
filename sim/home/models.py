from audioop import reverse
from distutils.command.upload import upload
from email.headerregistry import Address
from email.mime import image
from operator import length_hint
from pickle import TRUE
from pydoc import describe
from django.db import models
from django.urls import reverse
from home.fields import ThumbnailImageField

# Create your models here.
class town(models.Model):
    name = models.CharField('',max_length=30)
    description = models.CharField('One Line Description' , max_length=100, blank=True)
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='OWNER', blank=True,null=True)


    class Meta:
        ordering= ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:town_detail', args= (self.id,))

class home(models.Model):
    town = models.ForeignKey(town, on_delete=models.CASCADE)
    title = models.CharField('TITLE',max_length=30)
    description =models.TextField('home describe', blank=True)
    image = ThumbnailImageField(upload_to = 'home/%Y%m')
    upload_dt = models.DateField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='OWNER', blank=True,null=True)
    lat = models.FloatField('latitude', blank=True,null=True)
    lng = models.FloatField('longtite', blank=True,null=True)

    class Meta:
        ordering= ('title',)
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home:home_detail', args= (self.id,))

