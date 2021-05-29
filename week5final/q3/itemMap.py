import pandas as pd 
import numpy as np 

dataFrame  = pd.read_excel('German_Credit.xlsx')
x = dataFrame["CreditAmount"]
y = dataFrame["DurationOfCreditInMonths"]

for i in range(len(x)):
    print(f"{x[i]}\t{y[i]}")

    