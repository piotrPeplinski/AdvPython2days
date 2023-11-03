import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/catalogue/category/books_1/index.html'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

base_url = 'https://books.toscrape.com/catalogue/'

article = soup.find('article', class_='product_pod')
link = article.find('a').get_attribute_list('href')[0][6:]

book_url = base_url + link

r = requests.get(book_url)
book_soup = BeautifulSoup(r.text, 'html.parser')

ratings_enum = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}

title = book_soup.find('h1').text
price = book_soup.find('p', class_='price_color').text[2:]
stock = book_soup.find('p', class_='instock').text.split('(')[1].split(' ')[0]
rating_key = book_soup.find(
    'p', class_='star-rating').get_attribute_list('class')[1]
rating = ratings_enum[rating_key]

