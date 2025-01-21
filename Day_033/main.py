# On day 33, the concept of API was introduced, this is a small script that makes calls to the ISS Overhead API.

# The ISS is a stelite that is on constant movement around the world. Through this script, an e-mail is sent
# to the receiver specified on the .env file when the ISS is close to the specified geographic location.

from dotenv import load_dotenv
import datetime as dt
import os
import requests
import smtplib

BUFFER = 5

LAT = 41.157944
LONG = -8.629105

load_dotenv()

PASSWORD = os.getenv("sender_password")
RECEIVER = os.getenv("receiver_email")
SENDER = os.getenv("sender_email")
SMTP_SERVER = os.getenv("sender_server_smtp")


def get_iss_position(data):
    """Get the position of the International Space Station (ISS) from provided data.

    This function extracts the latitude and longitude of the ISS from
    the provided data dictionary, which is expected to contain the
    current position of the ISS.

    Args:
        data (dict): A dictionary containing the ISS position data,
        which must include the key "iss_position" with sub-keys
        "latitude" and "longitude".

    Returns:
        tuple: A tuple containing the latitude and longitude of the ISS
        as floats. The first element is the latitude, and the second
        element is the longitude.

    Raises:
        KeyError: If the expected keys ("iss_position", "latitude", 
        or "longitude") are not found in the provided data.
    """

    iss_lat = data["iss_position"]["latitude"]
    iss_long = data["iss_position"]["longitude"]

    return (float(iss_lat), float(iss_long))

def get_time_now(data):
    sunrise = data["results"]

def is_iss_close(pos):
    """Determine if the ISS is close to a specified position.

    This function checks if the given position (latitude and longitude)
    is within a defined buffer distance from the predefined latitude
    and longitude of a specific location.

    Args:
        pos (tuple): A tuple containing the latitude and longitude of
        the ISS as floats. The first element is the latitude, and the
        second element is the longitude.

    Returns:
        bool: True if the ISS is within the buffer distance of the
        specified position, False otherwise.
    """

    if LAT - BUFFER <= pos[0] <= LAT + BUFFER:
        if LONG - BUFFER <= pos[1] <= LONG + BUFFER:
            return True
    return False


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

def is_dark(sunrise, sunset):
    """Determine if it is currently dark based on sunrise and sunset times.

    This function checks the current hour against the provided sunrise
    and sunset times to determine if it is dark outside. It considers
    it dark if the current time is either after sunset or before sunrise.

    Args:
        sunrise (int): The hour of sunrise in 24-hour format (0-23).
        sunset (int): The hour of sunset in 24-hour format (0-23).

    Returns:
        bool: True if it is dark (current time is outside the range
        of sunrise to sunset), False otherwise.
    """
    time_now = dt.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

parameters = {"lat": LAT, "lng": LONG, "formatted": 0}

iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()

iss_data = iss_response.json()

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
sun_response.raise_for_status()

sun_data = sun_response.json()

sunrise = sun_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sun_data["results"]["sunset"].split("T")[1].split(":")[0]

if is_dark(sunrise, sunset):
    pass

iss_pos = get_iss_position(iss_data)

print(f"Data {sunrise}")

if is_iss_close(iss_pos):
    email_body = f"Subject:The ISS is close!\n\nLook up!\nThe ISS is at {iss_pos}"
    send_email(email_body)
else:
    print(f"The ISS is far..!\nCurrently at {iss_pos}")
