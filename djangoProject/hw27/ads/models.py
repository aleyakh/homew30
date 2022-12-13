from django.db import models


class Ads(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=15)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=90)
    is_published = models.BooleanField()


class Categories(models.Model):
    name = models.CharField(max_length=20)
