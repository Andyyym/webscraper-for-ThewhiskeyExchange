from bs4 import BeautifulSoup
import requests
import json

baseurl = 'https://www.thewhiskyexchange.com/'

productlinks = []

for x in range(1, 2):  # Currently only set to scrape the first page of the website, you can increase the value to your liking
    r = requests.get(
        f'https://www.thewhiskyexchange.com/c/465/red-wine?pg={x}')
    soup = BeautifulSoup(r.content, 'lxml')

    productlist = soup.find_all('li', class_='product-grid__item')

    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])


whiskeylist = []
for link in productlinks:

    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'lxml')

    name = soup.find('h1', class_='product-main__name').text.strip()
    description = soup.find(
        'div', class_='product-main__description').text.strip()
    price = soup.find('p', class_='product-action__price').text.strip()
    try:
        rating = soup.find('div', class_='review-overview').text.strip()

    except:
        rating = 'No Rating'

    Whiskey = {
        'Name': name,
        'Description': description,
        'Rating': rating,
        'Price': price
    }

    whiskeylist.append(Whiskey)
    print('Saving:', Whiskey['Name'])

with open('winedata.json', 'w') as f:
    json.dump(whiskeylist, f)
