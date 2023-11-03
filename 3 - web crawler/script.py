import pickle

with open(r'/Users/peplaj/Desktop/nobleMaterials/adv2days/3 - web crawler/books_df.pickle','rb') as file:
    df = pickle.load(file)

df.sort_values('rating', inplace=True)

print(df)