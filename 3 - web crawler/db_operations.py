import sqlite3
import pickle
import pandas as pd

with open(r'/Users/peplaj/Desktop/nobleMaterials/adv2days/3 - web crawler/books_df.pickle', 'rb') as file:
    df = pickle.load(file)


connection = sqlite3.connect('books.sqlite')
query = "SELECT * FROM books"
#WRITE
#df.to_sql('books', connection, if_exists='replace', index=False)
books = pd.read_sql(query, connection)
print(books)



connection.close()

