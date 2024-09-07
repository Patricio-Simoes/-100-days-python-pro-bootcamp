# The task of day 8 was creating a script that encrypts and decrypts messages using the Ceaser's cypher algorithm.
# To achieve this, the user has to provide a valid message and shift number.

from ascii_art import logo
from external import alphabet
import sys


# * Encrypts the message with the given shift number.
def encrypt(message, shift):
    encrypted_message = []
    message = message.lower()
    for letter in message:
        if letter in alphabet:
            shifted_index = alphabet.index(letter) + int(shift)
            shifted_letter = alphabet[shifted_index % len(alphabet)]
            encrypted_message.append(shifted_letter)
        else:
            encrypted_message.append(letter)
    return encrypted_message


# * Decrypts the message with the given shift number.
def decrypt(message, shift):
    decrypted_message = []
    message = message.lower()
    for letter in message:
        if letter in alphabet:
            shifted_index = alphabet.index(letter) - int(shift)
            shifted_letter = alphabet[shifted_index % len(alphabet)]
            decrypted_message.append(shifted_letter)
        else:
            decrypted_message.append(letter)
    return decrypted_message


# ? Program starts here.

exit_status = False

print(logo)

while not exit_status:
    opt = input("1. Encrypt\n2. Decrypt\n3. Exit\n: ")
    if opt == "1":
        message = input("Type your message:")
        shift = input("Type the shift number:")
        if shift.isdigit():
            output = "".join(encrypt(message, shift))
            print(f"Encrypted message: {output}\n")
        else:
            print("Error: The value you entered in invalid.")
    elif opt == "2":
        message = input("Type your message:")
        shift = input("Type the shift number:")
        if shift.isdigit():
            output = "".join(decrypt(message, shift))
            print(f"Decrypted message: {output}\n")
        else:
            print("Error: The value you entered in invalid.")
    elif opt == "3":
        print("Goodbye...")
        exit_status = True
