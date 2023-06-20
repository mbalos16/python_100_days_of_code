import pandas as pd

df = pd.read_csv("day_25/exercise25_2_2018_central_park_squirrel_census_data.csv")

gray_squirrel = (df["Primary Fur Color"] == "Gray").sum()
red_squirrel = (df["Primary Fur Color"] == "Cinnamon").sum()
black_squirrel = (df["Primary Fur Color"] == "Black").sum()


squirrel_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrel, red_squirrel, black_squirrel],
}

df_summary = pd.DataFrame(squirrel_dict)
df_summary.to_csv("day_25/squirrel_colors_summary.csv", index=False)
