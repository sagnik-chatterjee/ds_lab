import pandas as pd 
import numpy as np 

dates = pd.date_range('20210224',periods=100)

df = pd.DataFrame(np.random.randn(100,4),index=dates,columns=list('ABCD'))

##to print the first 5 records 
print(df.head())

#print the last 5 records 
print(df.tail())

##view the index 
print(df.index)

## to view thecolumns names 
print(df.columns)

##transpose the dataframe 
print(df.T)

## sorting by the axis 
print(df.sort_index(axis=1,ascending=False))

##sorting by the values 

print(df.sort_values(by='B'))

## slicing th rows 
print(df[0:3])

## slicing with index name 
print(df['20210224':'20210224'])

#slicing with row and clolumn index (2d matrix)
print(df.iloc[0])

##fetch 1 st row and first 2 cols 
print(df.iloc[0:2])

#fetch 1st row ,1st col element (single element)
print(df.iloc[0,0])

##selecting a single column 
print(df['A'])

#selecting more than one col
print(df[['A','B']])

##selecting moe than 1 ol ,with selected number of records 
print(df[['A','B']][:5])

## boolean indexing 

#fetch all pos values of A col
print(df[df.A>0])

##deleting a row or col  
##delete col A
df.drop('A',axis=1,inplace=True)
print(df)

