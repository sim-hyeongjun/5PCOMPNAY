from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify
'''
# Create your models here.
class poll(models.Model):
    title = models.CharField(max_length=200)
    link =  models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    def __str__(self):
        return self.title
'''

# Create your models here.
class News(models.Model):
    title = models.CharField('TITLE', max_length=200)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=1000, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'Newss'
        db_table = 'poll_Newss'
        ordering = ('-modify_dt',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('poll:News_detail', args=(self.slug,))
    
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    