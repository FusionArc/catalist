from django.db import models

class Asset(models.Model):
    cat_id = models.CharField(max_length=200)

class Brand(models.Model):
    name = models.CharField(max_length=200)

class Maker(models.Model):
    name = models.CharField(max_length=200)
