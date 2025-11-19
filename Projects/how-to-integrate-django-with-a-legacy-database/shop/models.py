from django.db import models

# Create your models here.


class ShopProduct(models.Model):
    title = models.CharField(max_length=60)

    class Meta:
        managed = True # change this to true or remove completely, default is True
        db_table = 'shop_product'