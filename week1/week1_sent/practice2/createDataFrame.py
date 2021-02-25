import pandas as pd 

data =[
  ["Dinesh",10],
  ["Nithya",12],
  ["Raji",13]
]

df=pd.DataFrame(data, columns=['Name','Age'])

##to print the top 5 entries
print(df.head())
#to print the bottom 5 entries 
print(df.tail())

