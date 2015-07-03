#!/usr/bin/env python

from lxml import html
import requests
import time

# @TODO:Make list of User-Agent and randomly attach User-Agent for every request
HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}


def parse_content(place, area):
    areas = area.split(',')

    for area in areas:
        page = requests.get(
            'http://property.sulekha.com/property-in-'+ area.replace(" ", "-") +'-'+ place +'-for-rent',
            headers=HEADERS)

        tree = html.fromstring(page.text)

        product_url_list = tree.xpath('//li/div/div/h3/a/@href')

        for link in product_url_list:
            # Crawling hits the website to get all the results
            # This may lead your IP to be blocked by host company
            # To prevent this we are making small delay of 10 seconds between two
            # consecutive requests
            # Also setting headers in request to make host feel that a request
            # is coming from browser
            time.sleep(10)
            page = requests.get(
                'http://property.sulekha.com' + link,
                headers=HEADERS)

            tree = html.fromstring(page.text)

            product_url = tree.xpath('string(//meta[@property="og:url"]/@content)')
            from_site = tree.xpath('string(//meta[@property="og:title"]/@content)')
            description = tree.xpath('string(//meta[@name="description"]/@content)')
            price = tree.xpath('string(//div[@class="container"]/div[4]/div[1]/div[2]/div[1]/span[3]/text())')
            bedrooms = tree.xpath('string(/html/body/div[4]/div[4]/div[1]/div[1]/ul/li[2]/span[2]/text())')
            posted_on = tree.xpath('string(/html/body/div[4]/div[3]/span/small/text())').split("on")

            # @alok  This is for testing purpose and need to be removed once entire app is developed
            print '\n\n'
            print 'product_url:', product_url.strip()
            print 'from_site:', from_site.strip()
            print 'description:', description.strip()
            print 'price:', price.strip()
            print 'bedrooms:', bedrooms.strip()
            print 'posted_on:', posted_on[1].strip()
            print '---------------------------------------------------'

if __name__ == '__main__':
    place = raw_input('Enter city: ').capitalize()
    area = raw_input('Enter area (For Multiple area enter , seprated): ')
    parse_content(place, area)
