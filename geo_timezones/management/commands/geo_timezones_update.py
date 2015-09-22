import sys

from django.contrib.gis.gdal import DataSource
from django.core.management.base import BaseCommand

from ...models import Timezone

__author__ = 'Alex Malyshev <malyshevalex@gmail.com>'


class Command(BaseCommand):

    help = 'Updates timezones db'

    def add_arguments(self, parser):
        # http://efele.net/maps/tz/world/
        parser.add_argument('shp_filename', type=str)

    def handle(self, *args, **options):
        shape_file_name = options['shp_filename']
        print('Updating timezone database from {}'.format(shape_file_name))
        ds = DataSource(shape_file_name)
        layer = ds[0]
        q = len(layer)
        n = 0
        Timezone.objects.all().delete()
        for feature in layer:
            Timezone.objects.create(
                timezone=feature.get('TZID'),
                geom=feature.geom.geos,
            )
            n += 1
            self._update_progress(n, q)

    @staticmethod
    def _update_progress(n, q):
        if sys.stdout.isatty():
            sys.stdout.write('\r[{0: <20}] {1} of {2}'.format('#' * round(20*n/q), n, q))
            if n == q:
                sys.stdout.write('\n\r')
