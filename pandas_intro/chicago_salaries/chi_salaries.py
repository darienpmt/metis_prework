import numpy as np
import pandas as pd

headers = ['name', 'title', 'department', 'salary']
chicago = pd.read_csv('city-of-chicago-salaries.csv', header=0, names=headers, converters={'salary': lambda x: float(x.replace('$', ''))})

def ranker(df):
    """Assigns a rank to each employee based on salary, with 1 being the highest paid.
    Assumes the data is DESC sorted."""

    df['dept_rank'] = np.arange(len(df)) + 1
    return df

chicago.sort_values('salary', ascending=False, inplace=True)
chi = chicago.apply(ranker)
print(chi)



