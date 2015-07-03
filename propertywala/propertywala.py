from lxml import html
import requests
import time


# @TODO:Make list of User-Agent and randomly attach User-Agent for requests
# User-Agent is used to show that the request is coming from browser.
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}


def check_index_range(value):
    try:
        return value[0].strip()
    except IndexError:
        return None


def check_list_range(tree):
    if "Project/Society:" == tree.xpath(
       '//*[@id="PropertyAttributes"]/li[1]/text()')[0].strip():
        return 1
    else:
        return 0


def parse_content(city, area):

    for location in area:
        url = 'http://www.propertywala.com/properties/type' \
            '-residential_apartment_flat/for-rent/' \
            'location-%s_%s/bedrooms-2/price-4' % (location, city)
        page = requests.get(url)
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
                                headers=HEADERS)
            tree = html.fromstring(page.text)

            i = check_list_range(tree)

            product_url = check_index_range(tree.xpath(
                '//meta[@property="og:url"]/@content'))
            product_id = "propertywala_" + check_index_range(tree.xpath(
                '//meta[@property="og:url"]/@content')).split('/')[-1:][0]
            title = check_index_range(tree.xpath(
                '//meta[@property="og:title"]/@content'))
            location = check_index_range(tree.xpath(
                '//div[@id="PropertyContent"]/div/section/header/h4/text()'))
            no_of_bedroom = check_index_range(tree.xpath(
                str(
                    '//div[@id="PropertyContent"]/div/section/ul/li[%s]/span/text()'
                ) % (2 + i)))
            rent = check_index_range(tree.xpath(
                str(
                    '//div[@id="PropertyContent"]/div/section/ul/li[%s]/span/text()'
                ) % (4 + i)))
            description = check_index_range(tree.xpath(
                '//div[@id="PropertyContent"]/div/section[2]/div/text()'
            ))
            date = check_index_range(tree.xpath(
                '//aside[@id="PropertySidebar"]/section/ul/li[1]/time/@datetime'
            )).split(" ")[0]

            # This is only for testing pusrpose will be removed later.
            print "\n --------------------------------------------------------"
            print "Product Id :", product_id
            print "Product Url :", product_url
            print "Title :", title
            print "Date :", date
            print "Location :", location
            print "Bedrooms :", no_of_bedroom
            print "Rent :", rent
            print "Description :", description
            print "-----------------------------------------------------------"

if __name__ == '__main__':
    city = raw_input("Enter the city :").lower()
    locations = raw_input("Enter area's :").lower()
    area = locations.split(',')

    parse_content(city, area)
