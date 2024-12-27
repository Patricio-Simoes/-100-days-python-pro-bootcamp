# Day 26 was focused on list conprehension.
# Here, the user inputs a word and the code makes use of pandas, list conprehension
# and dictionaries to return the NATO phonetic code for that word.

import pandas
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
NATO_FILE = os.path.join(PROJECT_DIR, "data", "nato_phonetic_alphabet.csv")


def read_file(file):
    """
    Read a CSV file and return its contents as a DataFrame.

    :param file: The path to the CSV file (str).
    :return: A pandas DataFrame containing the file's data.
    """
    with open(file, "r") as f:
        return pandas.read_csv(f)


def phonetize(input):
    """
    Convert each letter of the input string to its corresponding NATO phonetic code.

    :param input: The input string to be phonetized (str).
    :return: A list of NATO phonetic code words corresponding to each letter in the input.
    """
    phonetized_list = []
    for letter in input:
        phonetized_list.append(NATO_DICT[letter.upper()])
    return phonetized_list


raw_file_data = read_file(NATO_FILE)

NATO_LETTERS = raw_file_data["letter"].str.upper().tolist()
NATO_WORDS = raw_file_data["code"].str.capitalize().tolist()

NATO_DICT = {letter: code for (letter, code) in zip(NATO_LETTERS, NATO_WORDS)}

word = ""

while len(word) == 0:
    word = input("Enter a word: ")

print(f"Here are the phonetic code words for {word}: {phonetize(word)}")
