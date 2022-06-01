from re import T
from django.db import models
from djmoney.models.fields import MoneyField
from djgeojson.fields import PolygonField


class Provider(models.Model):

    name = models.CharField(max_length=64, verbose_name="Name")
    email = models.CharField(max_length=100, verbose_name="Email")
    phone_number = models.CharField(max_length=100, verbose_name="Phone Number")
    language = models.CharField(max_length=64, verbose_name="Language")
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='USD',
        verbose_name="Price"
        )
    
    def __str__(self):
        return str(self.name)


class ServiceArea(models.Model):
    polygon_name = models.CharField(
        max_length=64,
        verbose_name="Polygon Name"
        )
    polygon = PolygonField(verbose_name="Geo Polygon")
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        related_name="service_area"
        )
    
    def __str__(self):
        return str(self.polygon_name)
