# /project_name/app_name/utils/scraper.py

from Scripts import (sulekha,
                     magicBricks,
                     propertywala,
                     housing)

CITY = "PUNE"
AREAS = ["Hadapsar", "Warje", "Viman Nagar", "Wakad"]


def housing_officials():
    """Scrape for a list of current officeholders using an officials API"""
    housing.parse_content(CITY, AREAS)
    return True


def magicbricks_officials():
    """Scrape for a list of current officeholders using an officials API"""
    magicBricks.parse_content(CITY, AREAS)
    return True


def propertywala_officials():
    """Scrape for a list of current officeholders using an officials API"""
    propertywala.parse_content(CITY, AREAS)
    return True


def sulekha_officials():
    """Scrape for a list of current officeholders using an officials API"""
    sulekha.parse_content(CITY, AREAS)
    return True
