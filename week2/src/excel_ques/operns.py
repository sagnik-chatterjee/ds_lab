import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_excel("German Credit.xlsx", header=0,  engine="openpyxl")
print(df.head())
print(df.tail())

plt.scatter(df['CreditAmount'],df['DurationOfCreditInMonths'])
plt.xlabel('CreditAmount')
plt.ylabel('DurationOfCreditInMonths')
plt.show()#Figure_1


df['CreditAmount'].hist()
plt.show()#Figure_2




plt.boxplot(df,notch=True) 

f = df['Creditability'].value_counts()  
f.plot(kind='bar') 
plt.show()#Figure_3

f.plot(kind='pie') 
plt.show()#Figure_4
f = pd.crosstab(df['Creditability'],df['DurationOfCreditInMonths'])  
f.plot(kind='bar') 
plt.show() #Figure_5
