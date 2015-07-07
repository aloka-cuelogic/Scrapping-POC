#!/usr/bin/env python

import os, sys
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
sys.path.append(rootDir)
os.environ["DJANGO_SETTINGS_MODULE"] = "Scrapping_POC.settings"

from lxml import html
import requests
import time

from crawler.utils import add_property
import helper

# @TODO:Make list of User-Agent and randomly attach User-Agent for requests
# User-Agent is used to show that the request is coming from browser.


def parse_content(city, areas):

    for location in areas:
        url = 'http://www.propertywala.com/properties/type' \
            '-residential_apartment_flat/for-rent/' \
            'location-%s_%s/bedrooms-2/price-4' % (location, city)
        page = requests.get(url, headers=helper.HEADERS)
        tree = html.fromstring(page.text)

        links = tree.xpath(
            '//div[@class="searchList"]/article/header/h4/a/@href')

        for link in links:
            """
            Hitting the website continously might cause the IP getting
            blocked inorder to avoid it, we have made a delay of 10sec.
            """
            time.sleep(10)
            page = requests.get("http://www.propertywala.com" + link,
                                headers=helper.HEADERS)
            tree = html.fromstring(page.text)

            list_range = helper.check_list_range(tree)

            product_url = helper.check_index_range(tree.xpath(
                '//meta[@property="og:url"]/@content'))
            product_id = "propertywala_" + helper.check_index_range(tree.xpath(
                '//meta[@property="og:url"]/@content')).split('/')[-1:][0]
            title = helper.check_index_range(tree.xpath(
                '//meta[@property="og:title"]/@content'))
            location = helper.check_index_range(tree.xpath(
                '//div[@id="PropertyContent"]/div/section/header/h4/text()'))
            property_type = helper.check_index_range(tree.xpath(
                str(
                    '//div[@id="PropertyContent"]/div/section/ul/li[%s]/span/text()'
                ) % (2 + list_range)))
            monthly_rent = helper.check_range(
                helper.check_index_range(tree.xpath(
                    str(
                        '//div[@id="PropertyContent"]/div/section/ul/li[%s]/span/text()'
                    ) % (4 + list_range))))
            description = helper.check_index_range(tree.xpath(
                '//div[@id="PropertyContent"]/div/section[2]/div/text()'
            ))
            posted_on = helper.check_index_range(tree.xpath(
                '//aside[@id="PropertySidebar"]/section/ul/li[1]/time/@datetime'
            )).split(" ")[0]

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
                print "record inserted"


if __name__ == '__main__':
    city = raw_input("Enter the city :").lower()
    locations = raw_input("Enter area's :").lower()
    area = locations.split(',')

    parse_content(city, area)
