#!/usr/bin/env python

from lxml import html
import requests
import time
from datetime import datetime
from crawler.utils import add_property

# @TODO: Make list of User-Agent and randomly attach
#        User-Agent for every request
HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}


def parse_content(city, area):
    for area in areas:
        page = requests.get(
            'http://property.sulekha.com/property-in-' +
            area.replace(" ", "-") + '-' + city + '-for-rent',
            headers=HEADERS)

        tree = html.fromstring(page.text)

        product_url_list = tree.xpath('//li/div/div/h3/a/@href')

        for link in product_url_list:
            # Crawling hits the website to get all the results
            # This may lead your IP to be blocked by host company
            # To prevent this we are making small
            # delay of 10 seconds between two
            # consecutive requests
            # Also setting headers in request to make host feel
            # that a request is coming from browser
            time.sleep(10)
            page = requests.get(
                'http://property.sulekha.com' + link,
                headers=HEADERS)

            tree = html.fromstring(page.text)

            product_url = tree.xpath(
                'string(//meta[@property="og:url"]/@content)').strip()
            product_id = product_url.strip().split('_')[1]
            title = tree.xpath(
                'string(/html/body/div[4]/div[3]/span/h1/text())').strip()
            location = tree.xpath(
                'string(/html/body/div[4]/div[4]/div[1]/div[1]/ul/li[8]/span[2]/text())').strip()
            site_name = tree.xpath(
                'string(//meta[@property="og:site_name"]/@content)').strip()
            description = tree.xpath(
                'string(//meta[@name="description"]/@content)').strip()
            monthly_rent = check_range(
                tree.xpath('/html/body/div[4]/div[4]/div[1]/div[2]/div/span[3]/text()'))
            property_type = tree.xpath(
                'string(/html/body/div[4]/div[4]/div[1]/div[1]/ul/li[2]/span[2]/text())').strip()
            posted_on = tree.xpath(
                'string(/html/body/div[4]/div[3]/span/small/text())').split("on")[1].strip()

            posted_on = datetime.strptime(posted_on, "%b %d, %Y")
            product_id = site_name + '_' + product_id

            property_context = {}
            property_context['adverties_id'] = product_id
            property_context['title'] = title
            property_context['property_url'] = product_url
            property_context['location'] = location
            property_context['description'] = description
            property_context['monthly_rent'] = monthly_rent
            property_context['property_type'] = property_type
            property_context['posted_on'] = posted_on

            if monthly_rent is not None:
                add_property(property_context)


def check_range(value):
    try:
        val = int(value[1].replace(",", "").strip())
        return val
    except ValueError:
        return None


if __name__ == '__main__':
    '''
    Getting place and area is temporary
    it will be removed once actual crawler is up
    as crawler will be taking care of it
    '''

    place = raw_input("Enter city: ").lower()
    areas = raw_input("Enter area (For multiple area enter ,' \
        'seprated values): ").lower()
    area = area.split(',')
    parse_content(place, area)
