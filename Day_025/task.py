# This is a simple script, made on day 25 to play around with files and the pandas module.

# import csv

import pandas

FILE = "data/weather_data.csv"
TARGET = "data/pandas_output.txt"

# def read_weather():
#     with open(FILE) as file:
#         csv_data = file.readlines()
#         return csv_data


# def read_weather():
#     with open(FILE) as file:
#         temperatures = []
#         data = csv.reader(file)
#         for row in data:
#             if row[1] != "temp":
#                 temperatures.append(row[1])
#         return temperatures


def read_weather():
    data = pandas.read_csv(FILE)
    # Returns data, mean and max temperatures.
    return data, data.temp.mean(), data["temp"].max()


def save_weather_data(data, mean, max_temp):
    day_with_max_temp = data[data.temp == max_temp].day.values[0]
    lines = [
        f"Average week temperature: {mean}",
        f"Max week temperature: {max_temp} º on {day_with_max_temp}"
    ]
    with open(TARGET, "w") as file:
        for line in lines:
            file.write(line + "\n")


data, mean, max_temp = read_weather()

save_weather_data(data, mean, max_temp)
