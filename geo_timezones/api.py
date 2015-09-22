from django.contrib.gis.geos import Point

from .models import Timezone

__author__ = 'Alex Malyshev <malyshevalex@gmail.com>'

__all__ = ('get_timezone_name_by_coordinates', )


def get_timezone_name_by_coordinates(lat, long):
    tz = Timezone.objects.find(Point(long, lat))
    return tz.timezone if tz else None

