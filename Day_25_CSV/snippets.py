import csv
import pandas


# temperatures = []

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)

#data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# ave_temp = sum(temp_list) / len(temp_list)
# print(ave_temp)
# max_temp = data["temp"].max()
# print(f"The max temp was {max_temp}")
# print(data["temp"].mean())

# print(data.day)

# print(data)
# print(data["temp"])

#print(data[data.day=="Monday"])
#print(data[data["temp"].max()])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp * (9 / 5) +32)

data = pandas.read_csv("Day_25_CSV/2018_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {"Fur Colour": ["Gray", "Red", "Black"],
                "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

sq_panda = pandas.DataFrame(data_dict)
sq_panda.to_csv("Colour_Count.csv")

#print(black_squirrels_count)


# #print(data["Primary Fur Color"])
# data_dict = data.to_dict()
# squirrel_colour = pandas.DataFrame(data_dict["Primary Fur Color"], ["Hectare Squirrel Number"])
# squirrel_colour.to_csv("Squirrel_Colours.csv")


# fur_colour = data["Primary Fur Color"]
# count = data["Hectare Squirrel Number"]
# print(count)
