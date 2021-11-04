import argparse
from bs4 import BeautifulSoup
import requests
import json

def parse_items_sold(text):
    '''
    >>> parse_items_sold('38 sold')
    38
    >>> parse_items_sold('14 watchers')
    0
    >>> parse_items_sold('38 sold')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text:
        return int(numbers)
    else:
        return 0
def parse_shipping(text):
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if '$' in text:
        numbers = '$'+ str(float(numbers)/100)
        return numbers
    elif 'Free' in text:
        numbers = '$'+ str(0)
        return numbers

# this if ststaement syas only run if the def runs correctly
if __name__ == '__main__':
    # get command line arguments
    # 


    parser = argparse.ArgumentParser(description='Download information from ebay and convert to json')
    parser.add_argument('search_term')
    parser.add_argument('--page_number', default = 10)
    args = parser.parse_args()
    print ('args.search_terms =', args.search_term)


    # a list of all items

    items = []

    # loop over the ebay search
    for page_number in range(1,int(args.page_number)+1):
        # building the url
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+ args.search_term + '&_sacat=0&_pgn='+ str(page_number)
        filename = args.search_term + str(page_number) + '.html'
        print("url =", url)
        
        # download the url
        r = requests.get(url)
        status = r.status_code
        print('status code =', status)
        
        # download the html strings
        html = r.text
        # print('html =', html[:50])

        # "process" the html

        soup = BeautifulSoup(html, 'html.parser')
        tag_items = soup.select('.s-item')
        for tag_item in tag_items:
            # print('tag_items =', tag_items)

            
            tag_names = tag_item.select('.s-item__title')
            name = None
            for tag in tag_names:
                name = tag.text
                print("tags.text =", tag.text)
            
            
            free_returns = False
            tags_freereturns = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturns:
                free_returns = True
            
            items_sold = None
            tags_items_sold = tag_item.select('.s-item__hotness')
            for tag in tags_items_sold:
                items_sold = parse_items_sold(tag.text)
            
            shipping = None
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)


            item = {
                'name': name,
                'free_returns': free_returns,
                'items_sold': items_sold,
                'shipping': shipping
            }
            
            items.append(item)
            
            for item in items:
                print('item =', item)

    filename = args.search_terms + ".json"
    with open(filename,'w') as f:
        json.dump(items, f)