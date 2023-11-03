import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import pickle

with open('links.json') as file:
    links = json.load(file)


df = pd.DataFrame({
    'title': [],
    'price': [],
    'rating': [],
    'stock': [],
})

ratings_enum = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
base_url = 'https://books.toscrape.com/catalogue/'

for link in links:

    book_url = base_url + link

    r = requests.get(book_url)
    book_soup = BeautifulSoup(r.text, 'html.parser')

    title = book_soup.find('h1').text
    price = book_soup.find('p', class_='price_color').text[2:]
    stock = book_soup.find('p', class_='instock').text.split(
        '(')[1].split(' ')[0]
    rating_key = book_soup.find(
        'p', class_='star-rating').get_attribute_list('class')[1]
    rating = ratings_enum[rating_key]

    row = {'title': title, 'price': float(
        price), 'stock': int(stock), 'rating': rating}

    df.loc[len(df)] = row

with open('books_df.pickle', 'wb') as file:
    pickle.dump(df, file)
