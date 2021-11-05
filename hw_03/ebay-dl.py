import argparse
from bs4 import BeautifulSoup
import requests
import json
import csv

def parse_items_sold(text): # creating the function that filters for only the amount sold
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
def parse_shipping(text): # creating the function that filters for only the price of shipping

    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if '$' in text:
        numbers = str(int(numbers))
        return numbers
    elif 'Free' in text:
        numbers = str(0)
        return numbers
def parse_price(text): # creating the function that filters for only the price of the good
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if '$' in text:
        numbers = str(int(numbers))
        return numbers
def parse_status(text): # creating the function that filters for the quality status of the good
    t = ''
    for char in text:
        t += char
    return t
# this if ststaement syas only run if the def runs correctly
if __name__ == '__main__':
    

    # get command line arguments
    parser = argparse.ArgumentParser(description='Download information from ebay and convert to json')
    parser.add_argument('search_term')
    parser.add_argument('--page_number', default = 10)
    parser.add_argument('--csv', action='store_true')
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
        

        # "process" the html
        soup = BeautifulSoup(html, 'html.parser')
        tag_items = soup.select('.s-item')
        for tag_item in tag_items:
            # print('tag_items =', tag_items)

            
            tag_names = tag_item.select('.s-item__title') # find name tag
            name = None
            for tag in tag_names:
                name = tag.text
                print("tags.text =", tag.text)
            
            
            free_returns = False
            tags_freereturns = tag_item.select('.s-item__free-returns') # find if this good has free return
            for tag in tags_freereturns:
                free_returns = True
            
            items_sold = None
            tags_items_sold = tag_item.select('.s-item__hotness') # find how many of this good are sold
            for tag in tags_items_sold:
                items_sold = parse_items_sold(tag.text)
            
            shipping = None
            tags_shipping = tag_item.select('.s-item__shipping') # find the shipping fee
            for tag in tags_shipping:
                shipping = parse_shipping(tag.text)

            price = None
            tags_price = tag_item.select('.s-item__price') # find the price of the good
            for tag in tags_price:
                price = parse_price(tag.text)
            
            status = None
            tags_status = tag_item.select('.SECONDARY_INFO') # find the quality status of the good
            for tag in tags_status:
                status = parse_status(tag.text)

            item = {
                'name': name,
                'price': price,
                'status': status,
                'shipping': shipping,
                'free_returns': free_returns,
                'items_sold': items_sold,
                
            }
            
            items.append(item)
            
            for item in items:
                print('item =', item)
    if args.csv:
        item_list = ['name', 'price', 'status', 'shipping', 'free_returns', 'items_sold']
        filename = args.search_term + '.csv' # create CSV file from the search term
        with open(filename,'w', encoding='UTF8', newline = '') as f:
            writer = csv.DictWriter(f,item_list)
            writer.writeheader()
            writer.writerows(items)
    else:
        filename = args.search_term + '.json' # create json file from the search term
        with open(filename,'w') as f:
            json.dump(items, f)
            
    