from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        str(self.name)


class Maker(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
       return str(self.name)


class Asset(models.Model):
    cat_id = models.CharField(max_length=200, unique=True)
    brand = models.ForeignKey(Brand, default='UNKNOWN', on_delete=models.SET_DEFAULT)
    maker = models.ForeignKey(Maker, default='UNKNOWN', on_delete=models.SET_DEFAULT)
    name = f'{brand}_{str(id)}'

    def __str__(self):
       return str(self.name)
