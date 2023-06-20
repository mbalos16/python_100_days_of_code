import pandas

data = pandas.read_csv("day_25/exercise25_1_weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# # Temperature average
# temp_list_len = len(temp_list)
# temp_sum =0
# for temperature in temp_list:
#     temp_sum += temperature

# average = temp_sum / temp_list_len
# print(average)

# # Temperature mean
# print(data["temp"].mean())

# # Get hold of the max
# print(data["temp"].max())

# # Get data in row
# print(data[data.day == "Monday"])

# # Row of data with the highest temp in the week
# max = data["temp"].max()
# print(data[data.temp == max])

# Get Monday temp in Celsius
# monday = data[data.day == "Monday"]
# monday.temp = int(monday.temp)
# monday_temp_F = monday_temp * 9 / 5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "Students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)