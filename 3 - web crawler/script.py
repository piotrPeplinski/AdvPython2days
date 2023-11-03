import pickle
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functools import partial

with open(r'/Users/peplaj/Desktop/nobleMaterials/adv2days/3 - web crawler/books_df.pickle', 'rb') as file:
    df = pickle.load(file)

df.sort_values('price', inplace=True)

ratings = df['rating']
prices = df['price']
stocks = df['stock']

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

current_chart = None


def show_chart(y_axis, title, y_label):
    global current_chart
    if current_chart:
        current_chart.get_tk_widget().destroy()
        current_chart = None
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(prices, y_axis)
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel('Price')
    ax.grid(True)

    canvas = FigureCanvasTkAgg(fig, chart_frame)
    canvas.get_tk_widget().pack()
    canvas.draw()
    current_chart = canvas


ratings_btn = ttk.Button(root, text='Show ratings chart',
                         command=partial(show_chart, ratings, 'Price impact on ratings', 'Rating'))
ratings_btn.pack(side=tk.TOP, padx=5, pady=5)

stocks_btn = ttk.Button(root, text='Show stocks chart', command=partial(show_chart, stocks, 'Price impact on stock', 'Stock'))
stocks_btn.pack(side=tk.TOP, padx=5, pady=5)


root.mainloop()
