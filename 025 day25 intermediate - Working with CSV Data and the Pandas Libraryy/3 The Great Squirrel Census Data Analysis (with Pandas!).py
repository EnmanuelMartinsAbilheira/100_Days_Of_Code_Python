# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# #average = sum(temp_list) / len(temp_list)
# #print(average)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get Data in columns
# print(data["condition"])
# print(data.condition)
#
# #Get Data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 5/9 + 32
# print(monday_temp_F)
#
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")  # create a new CSV with the new documentations of the students



#start here

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv") # Create a new CSV with the quantiti about central park squirrel