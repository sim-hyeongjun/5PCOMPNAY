from django.db import models

class Category(models.Model):
    ca_id = models.AutoField(primary_key=True)
    ca_name = models.CharField(max_length=200)

    class Meta:
        managed =False
        db_table ='category'

class post(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title= models.CharField(max_length=45)
    pos_content = models.CharField(max_length=45)
    created_at = models.DateField()
    post_img = models.CharField(max_length=200, blank=True, null=True)
    catagory =models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table ='post'

        