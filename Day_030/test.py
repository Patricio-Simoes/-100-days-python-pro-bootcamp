def calculate_bmi(height, weight):
    if height > 3:
        raise ValueError("Human height should not exceed 3 meters!")
    bmi = weight / height**2
    print(f"BMI: {bmi}")


try:
    file = open("file.txt")
    my_dict = {"key": "value"}
    print(my_dict["key"])
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file was closed.")

# calculate_bmi(4, 60)
