from lxml import html
import requests
import time


# User-Agent is used to show that the request is coming from browser.
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}


def check_index_range(value):
    try:
        return value[0].strip()
    except IndexError:
        return " NONE "


def parse_content(city, area):

    for location in area:

        url = 'http://www.indiaproperty.com/%s-rent-' \
              'properties-%s' % (city, location)

        page = requests.get(url)
        tree = html.fromstring(page.text)

        links = tree.xpath(
            '//div[@class="highlightslots"]/div[1]/div[2]/div[2]/p[1]/a/@href')

        for link in links:
            """
            Hitting the website continously might cause the IP getting
            blocked inorder to avoid it, we have made a delay of 10sec.
            """

            time.sleep(10)
            page = requests.get(link, headers=HEADERS)
            tree = html.fromstring(page.text)

            product_url = "indiaproperty_" + check_index_range(tree.xpath(
                '//link[@rel="canonical"]/@href'))
            title = check_index_range(tree.xpath(
                '//span[@class="txt15 clr6 linlinblock"]/text()'))
            bedroom = check_index_range(tree.xpath(
                '//div[@class="left txt14 paddl20"]/div[2]/text()'
            ))
            rent = check_index_range(tree.xpath(
                '//div[@class="left txt24 boldtxt clr6 font-pro paddt15 width650"]/span/text()'
            )[1].split(")"))
            product_id = "indiaproperty_" + check_index_range(tree.xpath(
                '//div[@class="txt12  clear"]/span[2]/text()'))
            date = check_index_range(tree.xpath(
                '//div[@class="txt12  clear"]/span[4]/text()'))
            description = check_index_range(tree.xpath(
                '//div[@class="txt14 clr6 line24 justify"]/div/text()'))
            location = check_index_range(tree.xpath(
                '//div[@class="left paddt10"]/div[2]/text()'))

            # This is only for testing pusrpose, will be removed later.
            print "\n -------------------------------------------------------"
            print "Title :", title
            print "product_url :", product_url
            print "Id :", product_id
            print "Posted On :", date
            print "Bedroom :", bedroom
            print "Rent :", rent
            print "Location :", location
            print "Description :", description
            print "----------------------------------------------------------"

if __name__ == '__main__':
    city = raw_input("Enter the city :").lower()
    locations = raw_input("Enter area's :").lower()
    area = locations.split(',')

    parse_content(city, area)
