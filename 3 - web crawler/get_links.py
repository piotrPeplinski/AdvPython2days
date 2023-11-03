import requests
from bs4 import BeautifulSoup
import json

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')


articles = soup.find_all('article', class_='product_pod')

links = []
for article in articles:
    link = article.find('a').get_attribute_list('href')[0][6:]
    links.append(link)


with open('links.json', 'w') as file:
    json.dump(links, file)
