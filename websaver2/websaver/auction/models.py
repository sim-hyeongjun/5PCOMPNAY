from django.db import models


class auctionData(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    img = models.CharField(max_length=20000, null=True)
    
    def __str__(self):
        return self.title