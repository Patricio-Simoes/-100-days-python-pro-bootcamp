# On day 35, a rain alert script was built.
# This script, makes use of the Open Weather API, to fetch weather data from a set of given coordinates.
# Thie data retrieved is the forecast of the weather in the next days in 3h periods.
# On this script, data for the next 12h is retrieved, (4 periods of 3h), and if any of those periods signals
# the possibility of rainning, then an email is sent using Python's smtplib, warning that it's going to rain.

# To use this script, you need to provide your own Open Weather API key, alongside your email credentials for smtplib. 

from dotenv import load_dotenv
import os
import requests
import smtplib

load_dotenv()

OPEN_WEATHER_API = "https://api.openweathermap.org/data/2.5/forecast"

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")
OPEN_WEATHER_TARGET_LAT = os.getenv("OPEN_WEATHER_TARGET_LAT")
OPEN_WEATHER_TARGET_LON = os.getenv("OPEN_WEATHER_TARGET_LON")

SMTP_SENDER_EMAIL = os.getenv("SMTP_SENDER_EMAIL")
SMTP_SENDER_PASSWORD = os.getenv("SMTP_SENDER_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_RECEIVER_EMAIL = os.getenv("SMTP_RECEIVER_EMAIL")

PARAMETERS = {
    "lat": -19.6167,
    "lon": 169.2667,
    "appid": OPEN_WEATHER_API_KEY,
    "cnt": "4",
}

def get_weather_data():
    """
    Fetches weather data from the Open Weather API.

    This function sends a GET request to the Open Weather API using the specified
    URL and parameters. It raises an exception if the request fails and returns
    the JSON response containing the weather data.

    :return: A dictionary containing the weather data in JSON format.
    :raises requests.exceptions.HTTPError: If the HTTP request returned an unsuccessful status code.
    """
    response = requests.get(url=OPEN_WEATHER_API, params=PARAMETERS)
    response.raise_for_status()

    return response.json()

def get_ids():
    """
    Extracts weather condition IDs from the fetched weather data.

    This function iterates through the weather data and populates the `weather_data`
    dictionary with the weather condition IDs for each time period specified in the
    PARAMETERS.

    :return: None
    """
    for i in range(0, int(PARAMETERS["cnt"])):
        weather_data[i] = json_data["list"][i]["weather"][0]["id"]

def is_rain_foreseen():
    """
    Checks if rain is forecasted based on the weather condition IDs.

    This function examines the weather condition IDs stored in the `weather_data`
    dictionary. If any ID indicates rain (less than 700), it returns a message
    indicating when rain is expected.

    :return: A string message indicating when rain is expected, or None if no rain is forecasted.
    """
    for time_period in weather_data:
        if weather_data[time_period] < 700:
            return f"It's foreseen to start raining in {3 * (time_period + 1)} hours. Remember to bring an umbrella! ☂️"

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
            conn.login(user=SMTP_SENDER_EMAIL, password=SMTP_SENDER_PASSWORD)
            conn.sendmail(
                from_addr=SMTP_SENDER_EMAIL,
                to_addrs=SMTP_RECEIVER_EMAIL,
                msg=content.encode("utf-8"),
            )
    except smtplib.SMTPException:
        print("An error occured during the SMTP operation.")

json_data = get_weather_data()

weather_data = {}

get_ids()

send_email(is_rain_foreseen())