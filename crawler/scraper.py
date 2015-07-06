# /project_name/app_name/utils/scraper.py

from Scripts import (sulekha,
                     magicBricks,
                     propertywala,
                     housing)

CITY = "PUNE"
AREAS = ["Hadapsar", "Warje", "Viman Nagar", "Wakad"]


def housing_officials():
    """Scrape for a list of current officeholders using an officials API"""
    print "I am inside housing_officials"
    print "===================="
    housing.parse_content(CITY, AREAS)
    return True


def magicbricks_officials():
    """Scrape for a list of current officeholders using an officials API"""
    print "I am inside magicbricks_officials"
    print "===================="
    magicBricks.parse_content(CITY, AREAS)
    return True


def propertywala_officials():
    """Scrape for a list of current officeholders using an officials API"""
    print "I am inside propertywala_officials"
    print "===================="
    propertywala.parse_content(CITY, AREAS)
    return True


def sulekha_officials():
    """Scrape for a list of current officeholders using an officials API"""
    print "I am inside sulekha_officials"
    print "===================="
    sulekha.parse_content(CITY, AREAS)
    return True
