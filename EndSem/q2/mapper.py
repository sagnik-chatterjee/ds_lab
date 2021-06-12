import sys
import pandas as pd

# loading the pandass data into a dataframe
df = pd.read_csv('covid_data_lab_ds.csv')

# notna is taken as some values may get nan values when counting
# is used directly with values
df = df[df['Country/Region'].notna()]
df = df[df['Confirmed'].notna()]

# getting the values stored in the column as a list
words1 = list(df['Country/Region'].values)
words2 = list(df['Confirmed'].values)

# mapping them and print the country and the confirmed cases in them
for (word1, word2) in zip(words1, words2):
    print(f'{word1} \t {word2}')
