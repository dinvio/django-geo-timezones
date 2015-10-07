from distutils.core import setup

setup(
    name='django-geo-timezones',
    version='0.1.2',
    packages=['geo_timezones', 'geo_timezones.management', 'geo_timezones.management.commands','geo_timezones.migrations' ],
    url='https://github.com/dinvio/django-geo-timezones',
    license='MIT',
    author='Alex Malyshev',
    author_email='malyshevalex@gmail.com',
    description='Reusable Django App for determining timezone by geo coordinates',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ]
)
