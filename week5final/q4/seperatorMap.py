import pandas as pd 
import numpy as np 

def dateframe_input(dataframe):
    for x in dataframe['age']:
        yield x 

def main(separator='\t'):
    dataFrame = pd.read_csv('heart_disease_data.csv')
    data = dateframe_input(dataFrame)
    for x in data:
        print('%s%s%d' %(x,separator,1))

if __name__=='__main__':
    main()