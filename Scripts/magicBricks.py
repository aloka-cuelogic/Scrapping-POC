#!/usr/bin/env python

"""
Sample Script to Scrap a site using python lxml and request module.
"""
import os, sys
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
sys.path.append(rootDir)
os.environ["DJANGO_SETTINGS_MODULE"] = "Scrapping_POC.settings"

import requests
import time

from crawler.utils import add_property
from lxml import html

import helper


def parse_content(place, areas):
    for area in areas:
        url_str = 'http://www.magicbricks.com/property-for-rent/residential-real-estate?' \
            'proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,' \
            'Studio-Apartment,Service-Apartment&Locality' \
            '=%s&cityName=%s&BudgetMin=5,000&BudgetMax=10,000' % (area, place)

        user_page = requests.get(url_str, headers=helper.HEADERS)
        tree = html.fromstring(user_page.text)

        product_urls = tree.xpath(
            '//div[contains(@class,"srpBlock") and contains(@class, "srpContentImageWrap")]/@onclick')

        for link in product_urls:
            link_url = link.split("'")

            # Crawling hits the website to get all the results
            # This may lead your IP to be blocked by host company
            # To prevent this we are making small delay of 10 seconds between two
            # consecutive requests
            # Also setting headers in request to make host feel that a request
            # is coming from browser
            time.sleep(10)

            page = requests.get(
                'http://www.magicbricks.com' + link_url[1], headers=helper.HEADERS)

            html_string = html.fromstring(page.text)

            product_url = 'https://www.magicbricks.com' + link_url[1] 
            from_site = html_string.xpath(
                '//meta[@property="og:title"]/@content')[0].strip()
            description = html_string.xpath(
                '//meta[@name="Description"]/@content')[0].strip()
            monthly_rent = helper.check_range(
                html_string.xpath(
                    '//*[@id="rightAgentH"]/div[2]/div[2]/div[3]/div[2]/ul/li[1]/div/span/text()')[0].strip())
            product_id = html_string.xpath(
                '//span[@class="lastPart"]/text()')[0].split(':')[1].strip()
            location = html_string.xpath(
                '//span[@class="place"]/text()')[0].strip()

            property_context = {}
            property_context['adverties_id'] = from_site + str(product_id)
            property_context['property_url'] = product_url
            property_context['location'] = location
            property_context['description'] = description
            property_context['monthly_rent'] = monthly_rent

            if monthly_rent is not None:
                add_property(property_context)
                print "record inserted"


if __name__ == '__main__':
    '''
    Getting place and area is temporary 
    it will be removed once actual crawler is up
    as crawler will be taking care of it
    '''
    place = raw_input('Enter city: ').capitalize()
    areas = raw_input('Enter area (For Multiple area enter , seprated): ')
    area = areas.split(',')
    parse_content(place, area)
