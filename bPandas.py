import pandas as pd


s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])

data = {
    'País': ['Portugal', 'Peru', 'Chile'],
    'Capital': ['Lisboa', 'Lima', 'Santiago'],
    'População': [751000, 1120000, 695000]
    }

df = pd.DataFrame(data, columns=['País', 'Capital', 'População'])

print(df.iloc[0][0])
print("Correto!")