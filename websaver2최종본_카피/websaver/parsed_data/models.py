# parsed_data/models.py
from django.db import models


class BlogData(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    link = models.CharField(max_length=200)
    img = models.CharField(max_length=20000, null=True)
    
    def __str__(self):
        return self.title
    

    