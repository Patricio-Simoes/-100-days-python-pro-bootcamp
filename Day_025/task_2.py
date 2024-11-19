# This script, reads data from the 2018 central park squirrel census squirrel data and separates the squirrels by
# primary color type.
# After this is done, a pandas data frame is created with the sorted colors and the corresponding squirrel count, which
# is then saved into a csv file.

import pandas

SQUIRREL_DATA = "data/2018_Squirrel_Data.csv"
TARGET_FILE = "data/2018_Sorted_Squirrel_Data.csv"


def read_data(file):
    return pandas.read_csv(file)


def filter_colors(colors):
    sorted_squirrel_data = {}
    for color in colors:
        # Discard entries with invalid info.
        if pandas.isna(color):
            pass
        # First entry of a new color.
        elif color not in sorted_squirrel_data:
            sorted_squirrel_data[color] = 1
        # Color already exists, adds 1 to the counter
        else:
            sorted_squirrel_data[color] += 1
    return sorted_squirrel_data


def save_data_to_file(data):
    data.to_csv(TARGET_FILE, index=False)


raw_data = read_data(SQUIRREL_DATA)

colors = raw_data["Primary Fur Color"].values

sorted_data = filter_colors(colors)

output = pandas.DataFrame(list(sorted_data.items()), columns=['Fur Color', 'Count'])

save_data_to_file(output)
