#!/usr/bin/env python

import os
import sys
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
sys.path.append(rootDir)
os.environ["DJANGO_SETTINGS_MODULE"] = "Scrapping_POC.settings"

from crawler.utils import add_property
from lxml import html

import requests
import time

import helper


def parse_content(city, areas):
    for area in areas:
        page = requests.get(
            'https://housing.com/in/rent/%s/%s' % (city, area),
            headers=helper.HEADERS)

        tree = html.fromstring(page.text)

        product_url_list = tree.xpath(
            '//div[@class="heading-content information"]/a[@href]/@href')[:2]

        for link in product_url_list:
            # Crawling hits the website to get all the results
            # This may lead your IP to be blocked by host company
            # To prevent this we are making small delay of 10 seconds between two
            # consecutive requests
            # Also setting headers in request to make host feel that a request
            # is coming from browser
            time.sleep(10)
            page = requests.get(link, headers=helper.HEADERS)

            tree = html.fromstring(page.text)

            product_url  = link
            from_site = tree.xpath(
                'string(//meta[@property="og:site_name"]/@content)').strip()
            description = tree.xpath(
                'string(//meta[@name="description"]/@content)').strip()
            monthly_rent = helper.check_range(
                tree.xpath('string(//div[@class="banner"]/div[1]/div[2]/div[1]/span[2]/text())').strip())
            property_id = tree.xpath(
                'string(//div[@class="apartment-header"]/div[2]/ul/li[4]/text())').strip()
            location = tree.xpath(
                'string(//div[@class="main-details-pane"]/div[@class="heading"]/div[1]/text())').strip()
            property_type = tree.xpath(
                'string(//ul[@class="breadcrumb prop-breadcrumb"]/li[3]/span/h3/a/span/text())').strip()

            property_context = {}
            property_context['adverties_id'] = from_site + property_id
            property_context['property_url'] = product_url
            property_context['location'] = location
            property_context['description'] = description
            property_context['monthly_rent'] = monthly_rent
            property_context['property_type'] = property_type

            if monthly_rent is not None:
                add_property(property_context)
                print "record inserted"

if __name__ == '__main__':
    '''
    Getting place and area is temporary 
    it will be removed once actual crawler is up
    as crawler will be taking care of it
    '''

    place = raw_input("Enter city: ").lower()
    areas = raw_input("Enter area (For multiple area enter ','"
                      "seprated values): ").lower()
    area = areas.split(',')
    parse_content(place, area)
