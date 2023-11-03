import pandas as pd

data = {
    'Name': ['John','Mary','Anna'],
    'Age': [38,29,67],
    'City': ['New York', 'Cracow', 'Chicago']
}

df = pd.DataFrame(data)
print(df['City'])