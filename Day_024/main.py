# Day 24 was all about files.
# In this script, two files are received:
#   - The first contains a list of names.
#   - The second contains a letter template.
# The goal was to start from the template file and write multiple letters, changing each subject's name,
# to the names read in the first file.

NAMES_FILE = "Input/Names/invited_names.txt"
OUTPUT_PATH = "Output/ReadyToSend"
PLACEHOLDER = "[name]"
TEMPLATE_FILE = "Input/Letters/starting_letter.txt"


def read_file(file):
    """
    Read the contents of a file and return each line as a list item.

    :param file: The path to the file to read.
    :return: A list of lines read from the file. Returns an empty list if an error occurs.
    """
    with open(file, "r") as file:
        try:
            return file.read().splitlines()
        except Exception as e:
            print(f"Error reading file: {e}")
            return []


def save_letter(file, content):
    """
    Write content to a specified file.

    :param file: The path to the file to write to.
    :param content: The content to write in the file.
    """
    with open(file, "w") as file:
        try:
            file.write(content)
        except Exception as e:
            print(f"Error writing to file: {e}")


# List of people to invite.
people = read_file(NAMES_FILE)
# Read the template file.
template = read_file(TEMPLATE_FILE)

for name in people:
    output = template[0].replace(PLACEHOLDER, name) + "\n"
    # Append the remaining lines of the template to the output.
    for line in template[1:]:
        output += line + "\n"
    save_letter(f"{OUTPUT_PATH}/letter_for_{name}", output)
