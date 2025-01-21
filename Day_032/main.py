# Day 32 was focused on exploring Python's smtplib & e-mail sending capabilities.
# By the end of the day, this script was created.
# This script is an automated happy birthday e-mail sender.
# It fetches template data from a csv file, using pandas and after making some changes
# to the template, it proceeds to send an e-mail to the e-mails of the contacts who's
# birthday is today.

from dotenv import load_dotenv
import datetime as dt
import os
import pandas as pd
import random as rand
import smtplib

load_dotenv()

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BIRTHDAYS_FILE_PATH = os.path.join(PROJECT_DIR, "data", "birthdays.csv")

TEMPLATE_1_FILE_PATH = os.path.join(
    PROJECT_DIR, "data/letter_templates", "letter_1.txt"
)
TEMPLATE_2_FILE_PATH = os.path.join(
    PROJECT_DIR, "data/letter_templates", "letter_2.txt"
)
TEMPLATE_3_FILE_PATH = os.path.join(
    PROJECT_DIR, "data/letter_templates", "letter_3.txt"
)

TEMPLATES = (TEMPLATE_1_FILE_PATH, TEMPLATE_2_FILE_PATH, TEMPLATE_3_FILE_PATH)

PASSWORD = os.getenv("sender_password")
RECEIVER = os.getenv("receiver_email")
SENDER = os.getenv("sender_email")
SMTP_SERVER = os.getenv("sender_server_smtp")


def get_date():
    """Get the current date.

    This function retrieves the current date and returns it as a tuple
    containing the year, month, and day.

    Returns:
        tuple: A tuple containing the year, month, and day (year, month, day).
    """
    now = dt.datetime.now()
    day = now.day
    month = now.month
    year = now.year
    return (year, month, day)


def get_birthdays():
    """Retrieve birthdays from a CSV file.

    This function reads a CSV file containing birthday information and
    returns a list of dictionaries, where each dictionary represents a
    birthday entry.

    Returns:
        list: A list of dictionaries containing birthday information, or
            None if the file is not found.
    
    Raises:
        FileNotFoundError: If the birthdays CSV file cannot be found.
    """
    try:
        df = pd.read_csv(BIRTHDAYS_FILE_PATH)
    except FileNotFoundError:
        print(f"ERROR: the file {BIRTHDAYS_FILE_PATH} was not found!")
        return
    else:
        return df.to_dict(orient="records")


def compose_letter(template, name):
    """Compose a letter using a specified template.

    This function reads a letter template from a file, replaces placeholders
    with the provided name and sender's name, and returns the composed letter.

    Args:
        template (str): The file path of the letter template.
        name (str): The name to replace the [NAME] placeholder in the template.

    Returns:
        str: The composed letter with placeholders replaced, or None if the
            template file is not found.

    Raises:
        FileNotFoundError: If the template file cannot be found.
    """
    try:
        file = open(template, "r")
    except FileNotFoundError:
        print(f"ERROR: the file {BIRTHDAYS_FILE_PATH} was not found!")
        return
    else:
        content = file.read()
        file.close()
        return content.replace("[NAME]", name).replace("[SENDER]", "Patrício")


def send_email(content):
    """Send an email with the specified content.

    This function establishes a connection to the SMTP server, logs in using the
    sender's credentials, and sends an email to the specified receiver.

    Args:
        content (str): The content of the email to be sent.

    Raises:
        smtplib.SMTPException: If there is an error during the SMTP operation.
    """
    try:
        with smtplib.SMTP(SMTP_SERVER, port=587) as conn:
            conn.starttls()
            conn.login(user=SENDER, password=PASSWORD)
            conn.sendmail(
                from_addr=SENDER,
                to_addrs=RECEIVER,
                msg=content.encode("utf-8"),
            )
    except smtplib.SMTPException:
        print("An error occured during the SMTP operation.")


birthdays = get_birthdays()

date = get_date()

for birthday in birthdays:
    if birthday["month"] == date[1] and birthday["day"] == date[2]:
        letter = compose_letter(template=rand.choice(TEMPLATES), name=birthday["name"])
        email_body = f"Subject:Happy Birthday {birthday["name"]}\n\n{letter}"
        send_email(email_body)
