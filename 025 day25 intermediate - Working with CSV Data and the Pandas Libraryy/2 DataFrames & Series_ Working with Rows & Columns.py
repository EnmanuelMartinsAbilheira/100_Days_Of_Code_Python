import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

temp_list = data["temp"].to_list()
print(len(temp_list))

#average = sum(temp_list) / len(temp_list)
#print(average)

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in columns
print(data["condition"])
print(data.condition)

#Get Data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 5/9 + 32
print(monday_temp_F)


#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")  # create a new CSV with the new documentations of the students
