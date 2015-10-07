from django.db import models
from django.contrib.gis.db.models import PolygonField, GeoManager

__author__ = 'Alex Malyshev <malyshevalex@gmail.com>'


class TimezoneManager(GeoManager):

    def find(self, point):
        return self.filter(geom__contains=point).first()


class Timezone(models.Model):

    timezone = models.CharField(max_length=30)
    geom = PolygonField()

    objects = TimezoneManager()

    def __str__(self):
        return self.timezone
