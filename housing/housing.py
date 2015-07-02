#!/usr/bin/env python

from lxml import html
import requests
import time

# @TODO:Make list of User-Agent and randomly attach User-Agent for every request
HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}


def parse_content(city, area):
    areas = area.split(',')
    for area in areas:
        page = requests.get(
            'https://housing.com/in/rent/%s/%s'% (city, area),
            headers=HEADERS)

        tree = html.fromstring(page.text)

        product_url_list = tree.xpath('//div[@class="heading-content information"]/a[@href]/@href')

        for link in product_url_list:
            # Crawling hits the website to get all the results
            # This may lead your IP to be blocked by host company
            # To prevent this we are making small delay of 10 seconds between two 
            # consecutive requests
            # Also setting headers in request to make host feel that a request is coming from browser
            time.sleep(10)
            page = requests.get(link, headers=HEADERS)

            tree = html.fromstring(page.text)

            product_url = tree.xpath('string(//meta[@property="og:url"]/@content)').strip()
            from_site = tree.xpath('string(//meta[@property="og:site_name"]/@content)').strip()
            description = tree.xpath('string(//meta[@name="description"]/@content)').strip()
            price = tree.xpath('string(//div[@class="banner"]/div[1]/div[2]/div[1]/span[2]/text())').strip()
            property_id = tree.xpath('string(//div[@class="apartment-header"]/div[2]/ul/li[4]/text())').strip()
            # @deepalib  This is for testing purpose and need to be removed once entire app is developed
            print '\n\n'
            print 'from_site:', from_site
            print 'product_url:', product_url
            print 'housing_id:', property_id
            print 'description:', description
            print 'price:', price
            print '---------------------------------------------------'

if __name__ == '__main__':
    '''
    Getting place and area is temporary 
    it will be removed once actual crawler is up
    as crawler will be taking care of it
    '''

    place = raw_input("Enter city: ").lower()
    area = raw_input("Enter area (For multiple area enter ','" \
                     "seprated values): ").lower()
    parse_content(place, area)
