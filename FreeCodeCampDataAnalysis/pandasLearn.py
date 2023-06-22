import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Pandas Series

# g7_pop = pd.Series([35.467,63.234,80.435,60.134,127.435,64.226,318.443])



# g7_pop.name = "G7 Population in millions"

# g7_pop.index = [
#     "Canada",
#     "France",
#     "Germany",
#     "Italy",
#     "Japan",
#     "United Kingdom",
#     "United States"
# ]

# print(g7_pop)



#Indexing

# g7_pop =pd.Series({
#     'Canada': 35.467,
#     'France': 63.951,
#     'Germany': 80.94,
#     'Italy': 60.665,
#     'Japan': 127.061,
#     'United Kingdom': 64.511,
#     'United States': 318.523
# }, name='G7 Population in millions')

# #print(g7_pop["Canada"])

# #Numeric positions can also be used, with iloc attribute

# #print(g7_pop.iloc[-1])



# #Conditional Selection 

# #print(g7_pop>70)

# result = g7_pop * 1000000

# #print(g7_pop[g7_pop > 70])

# #Data Frames
# # data frames a table but more look like a excel sheet(more information)

# g7_popDataF = df = pd.DataFrame({
#     'Population': [35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.523],
#     'GDP': [
#         1785387,
#         2833687,
#         3874437,
#         2167744,
#         4602367,
#         2950039,
#         17348075
#     ],
#     'Surface Area': [
#         9984670,
#         640679,
#         357114,
#         301336,
#         377930,
#         242495,
#         9525067
#     ],
#     'HDI': [
#         0.913,
#         0.888,
#         0.916,
#         0.873,
#         0.891,
#         0.907,
#         0.915
#     ],
#     'Continent': [
#         'America',
#         'Europe',
#         'Europe',
#         'Europe',
#         'Asia',
#         'Europe',
#         'America'
#     ]
# }, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])


# g7_popDataF.index = [
#     'Canada',
#     'France',
#     'Germany',
#     'Italy',
#     'Japan',
#     'United Kingdom',
#     'United States'
# ]

# col = g7_popDataF.columns
# indexes = g7_popDataF.index
# info = g7_popDataF.info()#give you information the structure of your data frame
# desc = g7_popDataF.describe() # give you a summary of the statistics of the data frame (mostly numeric)

# loc = g7_popDataF.loc['Canada'] # loc let you select rew by index
# iloc = g7_popDataF.iloc[-1] # iloc let you select rows by sequential position 


#Dropping
#Boolean 
#Adding
#Replacing
#Renaming

#Creating Columns
#g7_popDataF['GDP Per Capita'] = g7_popDataF['GDP'] / g7_popDataF['Population']


#reading csv


#bitCsv = pd.read_csv('data/btc-market-price.csv',header=None)#Header = None don't read the header from the csv file
#bitCsv.columns = ['Timestamp','Price']


#pd.to_datetime(bitCsv['Timestamp']).head()

#bitCsv['Timestamp'] = pd.to_datetime(bitCsv['Timestamp'])


#bitCsv.set_index('Timestamp',inplace=True)

#Easy Way

bitCsv = pd.read_csv(
    'data/btc-market-price.csv',
    header=None,
    names=['Timestamp','Price'],#Col names
    index_col=0,#The first col is the index of the data frame
    parse_dates=True#parse the date timestamp is a date is true so type is auto changed
)




#Data Cleaning


#More Visualizations






