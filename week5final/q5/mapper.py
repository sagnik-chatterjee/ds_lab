import numpy as np
import pandas as pd

dataframe = pd.read_csv("covid_19_data.csv")
country_name = dataframe["Country/Region"]
peak_cases = dataframe["Confirmed"]

for x in range(len(country_name)):
	print("%s\t%d" %(country_name[x],peak_cases[x]))