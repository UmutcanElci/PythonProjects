import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

sales_df = pd.read_csv("data/sales_data.csv")

#print(sales_df.head()) # Prints the initial few lines.This is often used to quickly see the structure


#print(sales_df.shape) # Prints the number of rows nad columns of the data (rows , cols)


#print(sales_df.info()) # Shows the name, data type and memory usage of each column in the data frame.


#print(sales_df.describe()) # provides a statistical summary of the data frame.

#print(sales_df["Unit_Cost"].describe())


#print(sales_df["Unit_Cost"].mean()) # average value

#print(sales_df["Unit_Cost"].median()) # median value

#sales_df["Unit_Cost"].plot(kind="box", vert= False, figsize=(14,6)) # plot for data visualization


#sales_df["Unit_Cost"].plot(kind="density", figsize=(14,6))



#ax = sales_df["Unit_Cost"].plot(kind="hist", figsize=(14,6))
#ax.set_ylabel("Numbre of Sales")
#ax.set_xlabel("Dollars")
#ax.axvline(sales_df["Unit_Cost"].mean(), color="red")
#ax.axvline(sales_df["Unit_Cost"].median(),color="green")

#print(sales_df["Age_Group"].value_counts()) #Counts how many times each unique value in the column is repeated and returns a Series as a result


#sales_df["Age_Group"].value_counts().plot(kind="pie",figsize=(6,6))


#ax = sales_df["Age_Group"].value_counts().plot(kind="bar",figsize=(14,6))
#ax.set_ylabel("Number of Sales")


#corr = sales_df.corr() #used to calculated the correlation between numeric columns in the data frame

# fig = plt.figure(figsize=(8,8))
# plt.matshow(corr,cmap="RdBu",fignum=fig.number)
# plt.xticks(range(len(corr.columns)), corr.columns,rotation="vertical")
# plt.yticks(range(len(corr.columns)),corr.columns)

