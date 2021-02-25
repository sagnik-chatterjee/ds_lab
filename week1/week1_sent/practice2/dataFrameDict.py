'''
creating adata frame using a dictionary
'''

import pandas as pd 
import numpy as np 

df1 = pd.DataFrame(
  {'A':pd.Timestamp('20210224'),
    'B':np.array([3]*4,dtype='int32'),
    'C':pd.Categorical(['Male','Female','Male','Female'])
    }
)

#print the shape i.e dimesion of the matrix 
print(df1.shape)
print(df1)

print(df1.dtypes)
print(df1.head()) ##print the first 5 records 

#print thje last 5 records
print(df1.tail())

print(df1.describe())

## print the transpose of the matrix 
print(df1.T)

