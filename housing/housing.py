#!/usr/bin/env python

from lxml import html
import requests
import time


HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}


def scrap_housing():
    place = raw_input('Enter city: ').lower()
    area = raw_input('Enter area (For multiple area enter ',' seprated values): ').lower()
    AREAS = area.split(',')
    for area in AREAS:
        page = requests.get(
            'https://housing.com/in/rent/%s/%s'% (place,area),
            headers=HEADERS)

        tree = html.fromstring(page.text)

        product_url_list = tree.xpath('//div[@class="heading-content information"]/a[@href]/@href')
        print product_url_list
        for link in product_url_list:
            time.sleep(10)
            page = requests.get(link,headers=HEADERS)

            tree = html.fromstring(page.text)

            product_url = tree.xpath('string(//meta[@property="og:url"]/@content)').strip()
            from_site = tree.xpath('string(//meta[@property="og:site_name"]/@content)').strip()
            description = tree.xpath('string(//meta[@name="description"]/@content)').strip()
            price = tree.xpath('string(//div[@class="banner"]/div[1]/div[2]/div[1]/span[2]/text())').strip()
            property_id = tree.xpath('string(//div[@class="apartment-header"]/div[2]/ul/li[4]/text())').strip()
            print '\n\n'
            print 'from_site:', from_site
            print 'product_url:', product_url
            print 'housing_id:', property_id
            print 'description:', description
            print 'price:', price
            print '---------------------------------------------------'

if __name__ == '__main__':
    scrap_housing()
