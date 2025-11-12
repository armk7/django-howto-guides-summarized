from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField("Title", max_length=60)
    description = models.TextField("Description", max_length=120)