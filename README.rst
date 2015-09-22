=============
Geo Timezones
=============

Geo timezones is a simple Django app to determine timezone by geographic coordinates.

Quick start
-----------

1. Add "geo_timezones" to your INSTALLED_APPS settings like this::

    INSTALLED_APPS = (
        ...
        'geo_timezones',
        ...
    )

2. Download SHP TZ_DATA file from http://efele.net/maps/tz/world/.

3. Run `python manage.py migrate` to create the timezones models.

4. Run `python manage.py geo_timezones_update --shp_filename=<your shp tz_data file>` to update timezones.

5. Use app in your code::

    ...
    from geo_timezones import get_timezone_name_by_coordinates
    ...

    timezone_name = get_timezone_name_by_coordinates(55.3424, 61.0034)  # lat, long

