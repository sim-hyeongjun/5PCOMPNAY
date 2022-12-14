
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify






# Create your models here.
class airport(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)
    
    class Meta:
        verbose_name = 'airport'
        verbose_name_plural = 'airports'
        db_table = 'airport'
    def get_previous(self):
        return self.get_previous_by_modify_dt()
    
    def get_next(self):
        return self.get_next_by_modify_dt()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
