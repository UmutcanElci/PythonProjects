import pandas as pd
import matplotlib.pyplot as plt
covid_df = pd.read_csv("covid19.csv")

dim = covid_df.shape #data frame (10902 row - 14 row )

vector_cols = covid_df.columns # columns of the dataset

#print(covid_df.head(15)) # print first 15 row 

#print(covid_df.info) # same thing like head function

covid_df_all_states = covid_df[covid_df["Province_State"] == "All States"]
covid_df_all_states = covid_df_all_states.drop("Province_State",axis=1)
covid_df_all_states_cumulative = covid_df_all_states[
    ["Date", "Continent_Name", "Two_Letter_Country_Code", "positive", "hospitalized", "recovered", "death", "total_tested"]
    ]


covid_df_all_states_cumulative_max = covid_df_all_states_cumulative.groupby(["Continent_Name", "Two_Letter_Country_Code"]).max().reset_index()
covid_df_all_states_cumulative_max = covid_df_all_states_cumulative_max[covid_df_all_states_cumulative_max["positive"] > 0]

continent_colors = {
    "Africa": "red",
    "Asia": "green",
    "Europe": "blue",
    "North America": "orange",
    "Oceania": "purple",
    "South America": "yellow"
}

colors = [continent_colors[continent] for continent in covid_df_all_states_cumulative_max["Continent_Name"]]

plt.scatter(covid_df_all_states_cumulative_max["Two_Letter_Country_Code"],
            covid_df_all_states_cumulative_max["death"],
            c=colors)

plt.xlabel("Two_Letter_Country_Code")
plt.ylabel("Maximum Death")
plt.title("Maximum Death by Country")

# Sort the dataframe by "death" column in descending order
sorted_df = covid_df_all_states_cumulative_max.sort_values(by="death", ascending=False)

# Select the top three countries
top_3_countries = sorted_df["Two_Letter_Country_Code"].head(3)

# Convert the country codes to a character vector
death_top_3 = top_3_countries.tolist()

