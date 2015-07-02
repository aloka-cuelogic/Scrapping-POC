from lxml import html
import requests
import time


HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}


place = raw_input('Enter city: ').capitalize()
area = raw_input('Enter area (For Multiple area enter , seprated): ')
AREAS = area.split(',')


for area in AREAS:
    page = requests.get(
        'http://property.sulekha.com/property-in-'+ area.replace(" ", "-") +'-'+ place +'-for-rent',
        headers=HEADERS)

    tree = html.fromstring(page.text)

    product_url_list = tree.xpath('//li/div/div/h3/a/@href')

    print product_url_list

    for link in product_url_list:
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

        print '\n\n\n\n'
        print 'product_url:', product_url.strip()
        print 'from_site:', from_site.strip()
        print 'description:', description.strip()
        print 'price:', price.strip()
        print 'bedrooms:', bedrooms.strip()
        print 'posted_on:', posted_on[1].strip()
