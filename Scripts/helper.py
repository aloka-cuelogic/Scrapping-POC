HEADERS = {'User-Agent':
           'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}

def check_range(value):
    try:
        val = int(value.replace(",", "").strip())
        return val
    except ValueError:
        return None
    except AttributeError:
    	return None


def check_index_range(value):
    try:
        return value[0].strip()
    except IndexError:
        return None
    except ValueError:
    	return None


def check_list_range(tree):
    if "Project/Society:" == tree.xpath(
       '//*[@id="PropertyAttributes"]/li[1]/text()')[0].strip():
        return 1
    else:
        return 0
