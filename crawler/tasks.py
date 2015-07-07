from celery.decorators import task
from crawler import scraper


@task
def housing_officials(*args):
    scraper.housing_officials(*args)


@task
def magicbricks_officials(*args):
    scraper.magicbricks_officials(*args)


@task
def propertywala_officials(*args):
    scraper.propertywala_officials(*args)


@task
def sulekha_officials(*args):
    scraper.sulekha_officials(*args)
