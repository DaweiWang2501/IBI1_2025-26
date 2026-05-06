import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change this path to the folder where your csv file is stored
os.chdir("C:/Users/ASUS/OneDrive - International Campus, Zhejiang University/桌面/大学/上课文件、手册及其分组/大一下/IBI 1/IBI1_2025-26/IBI1_2025-26/Practical 10")
# Import the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Check the dataset
print(dalys_data.head(5))
print(dalys_data.info())
print(dalys_data.describe())

# Show the third and fourth columns, Year and DALYs, for the first 10 rows
first_10_year_dalys = dalys_data.iloc[0:10, 2:4]
print(first_10_year_dalys)

# Afghanistan first 10 years: find the year with the maximum DALYs
max_row_afghanistan = first_10_year_dalys.loc[first_10_year_dalys["DALYs"].idxmax()]
print("Maximum DALYs in the first 10 Afghanistan rows:")
print(max_row_afghanistan)

# Comment: Across the first 10 years for Afghanistan, the maximum DALYs were recorded in the year printed above.

# Show all years for which DALYs were recorded in Zimbabwe
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print("Years recorded for Zimbabwe:")
print(zimbabwe_years)

# Comment: Zimbabwe data were recorded from 1990 to 2019.

# Data from 2019
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

# Find countries with maximum and minimum DALYs in 2019
max_2019 = recent_data.loc[recent_data["DALYs"].idxmax()]
min_2019 = recent_data.loc[recent_data["DALYs"].idxmin()]

print("Country with maximum DALYs in 2019:")
print(max_2019)

print("Country with minimum DALYs in 2019:")
print(min_2019)

# Comment: The countries with maximum and minimum DALYs in 2019 are printed above.

# Plot DALYs over time for the country with the maximum DALYs in 2019
max_country = max_2019["Entity"]
max_country_data = dalys_data.loc[dalys_data["Entity"] == max_country]

plt.figure()
plt.plot(max_country_data["Year"], max_country_data["DALYs"], "bo-")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs over time in " + max_country)
plt.xticks(max_country_data["Year"], rotation=-90)
plt.tight_layout()
plt.show()

# Extra question:
# What was the distribution of DALYs across all countries in 2019?

plt.figure()
plt.hist(recent_data["DALYs"], bins=20)
plt.xlabel("DALYs")
plt.ylabel("Number of countries")
plt.title("Distribution of DALYs across countries in 2019")
plt.tight_layout()
plt.show()

print("Summary statistics for DALYs across countries in 2019:")
print(recent_data["DALYs"].describe())