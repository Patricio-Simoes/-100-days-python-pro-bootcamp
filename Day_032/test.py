# This is a script for sending a motivational quote e-mail with Python.
# The e-mail is sent if today is equal to the specified day for sending quotes.
# To use it, you will need a .env file with the following credentials:
#   - sender_email : The e-mail you are sending the e-mail from.
#   - sender_password : The password for that e-mail, (use an app password).
#   - sender_server_smtp : The smtp server of your e-mail's provider.
#   - receiver_email : The e-mail you are sending the e-mail to.

from dotenv import load_dotenv
import datetime as dt
import os
import random
import smtplib

# Load environment variables from .env file.
load_dotenv()

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

QUOTES_FILE_PATH = os.path.join(PROJECT_DIR, "data", "quotes.txt")

PASSWORD = os.getenv("sender_password")
RECEIVER = os.getenv("receiver_email")
SENDER = os.getenv("sender_email")
SMTP_SERVER = os.getenv("sender_server_smtp")

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

TODAY = SATURDAY

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

def get_weekday():
    """Get the current weekday.

    This function returns the current day of the week as an integer, where Monday
    is 0 and Sunday is 6.

    Returns:
        int: The current weekday as an integer.
    """
    today = dt.datetime.now().weekday()
    return today


def get_quote():
    """Retrieve a random quote from the quotes file.

    This function reads quotes from a specified file and returns a randomly
    selected quote. If the file is not found, an error message is printed.

    Returns:
        str: A randomly selected quote, or None if the file is not found.
    """
    try:
        with open(QUOTES_FILE_PATH, "r") as file:
            quotes = file.readlines()
    except FileNotFoundError:
        print(f"ERROR: The file {QUOTES_FILE_PATH} was not found!")
        return
    else:
        quote = random.choice(quotes).strip()
        return quote
        
if get_weekday() == TODAY:
    email_content = f"Subject:Motivational Quote From Python\n\n{get_quote()}"
    send_email(email_content)