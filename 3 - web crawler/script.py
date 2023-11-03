import pickle
import matplotlib.pyplot as plt
import tkinter as tk

with open(r'/Users/peplaj/Desktop/nobleMaterials/adv2days/3 - web crawler/books_df.pickle', 'rb') as file:
    df = pickle.load(file)

df.sort_values('price', inplace=True)

ratings = df['rating']
prices = df['price']

# plt.plot(prices, ratings)
# plt.ylabel('Rating')
# plt.xlabel('Price')
# plt.title('Price correlation to rating')
# plt.show()

root = tk.Tk()
root.title('Book charts')
root.geometry('800x500')

chart_frame = tk.Frame(root)
chart_frame.pack(side=tk.LEFT, padx=10, pady=10)

ratings_btn = tk.Button(root, text='Show ratings chart')
ratings_btn.pack(side=tk.TOP, padx=5, pady=5)

stocks_btn = tk.Button(root, text='Show stocks chart')
stocks_btn.pack(side=tk.TOP, padx=5, pady=5)


root.mainloop()
