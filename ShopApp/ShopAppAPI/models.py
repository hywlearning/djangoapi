# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    slug= models.SlugField()
    title= models.CharField(max_length=255,unique=True)

    class Meta:
        managed = False
        db_table = 'tb_category'

    def __str__(self):
        return self.title
    
class TbMenu(models.Model):
    fd_id = models.AutoField(primary_key=True)
    fd_title = models.CharField(max_length=255, blank=True, null=True,unique=True)
    fd_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fd_inventory = models.SmallIntegerField(blank=True, null=True)
    fd_categoryid = models.ForeignKey(Category,on_delete=models.PROTECT,default=1)

    class Meta:
        managed = False
        db_table = 'tb_menu'


