# Day 24 was all about files.
# In this script two files are received:
#   - The first, contains a list of names.
#   - The second contains a letter template.
# The goal is to start from the template file and write multiple letters, changing each subject's name,
# to the names read in the first file.

NAMES_FILE = "Input/Names/invited_names.txt"
OUTPUT_PATH = "Output/ReadyToSend"
PLACEHOLDER = "[name]"
TEMPLATE_FILE = "Input/Letters/starting_letter.txt"


def read_file(file):
    """
    Tries to read the passed file and returns each line as a list item.
    @param file: Specifies the file to read from.
    @return: List with each line read.
    """
    with open(file, "r") as file:
        try:
            return file.read().splitlines()
        except Exception as e:
            print(f"Error reading file: {e}")
            return []


def save_letter(file, content):
    """

    @param file: Specifies the file to write to.
    @param content: Specifies the content to write in the file.
    """
    with open(file, "w") as file:
        try:
            file.write(content)
        except Exception as e:
            print(f"Error writing to file: {e}")


# List of people to invite.
people = read_file(NAMES_FILE)
# template[0] contains the line to be replaced.
template = read_file(TEMPLATE_FILE)

for name in people:
    output = template[0].replace(PLACEHOLDER, name) + "\n"
    i = 1
    while i < len(template):
        output += template[i] + "\n"
        i += 1
    save_letter(OUTPUT_PATH + "/letter_for_" + name, output)
