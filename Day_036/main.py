# On day 36, the goal was to create a script that was responsible for commuinicating
# with two different APIs.
# The first, used to fetch the stock prices of a given company, and the sconds, to fetch news
# related to that company, if there was a significant stock price increase/decrease on the previous day.
# These news, are processed and sent by email.

from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import requests
import smtplib

load_dotenv()

# Alpha Advantage's API is used to get daily stock prices.
ALPHA_ADVANTAGE_API = "https://www.alphavantage.co/query"
# NewsAPI.org is used to get news related to a topic.
NEWS_API = "https://newsapi.org/v2/everything"

GET_NEWS_RISE_PERCENTAGE = 5

NEWS_COUNT = "3"

COMPANY_NAME = "Tesla Inc"

ALPHA_PARAMETERS = {
    "symbol": "TSLA",
    "function": "TIME_SERIES_DAILY",
    "apikey": os.getenv("ALPHA_ADVANTAGE_API_KEY"),
}

NEWS_PARAMETERS = {
    "q": "Tesla Inc",
    "searchIn": "title",
    "pageSize": NEWS_COUNT,
    "sortBy": "publishedAt",
    "apiKey": os.getenv("NEWS_API_KEY"),
}

SMTP_SENDER_EMAIL = os.getenv("SMTP_SENDER_EMAIL")
SMTP_SENDER_PASSWORD = os.getenv("SMTP_SENDER_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_RECEIVER_EMAIL = os.getenv("SMTP_RECEIVER_EMAIL")


def get_dates():
    """
    Get the dates for yesterday and the day before yesterday.

    This function calculates the dates for yesterday and the day before yesterday
    in the format "YYYY-MM-DD".

    Returns:
        tuple: A tuple containing two strings:
            - The date for yesterday.
            - The date for the day before yesterday.
    """
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    day_before_yesterday = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")
    return (yesterday, day_before_yesterday)


def get_stock_prices(dates):
    """
    Retrieve the stock closing prices for the given dates.

    This function makes a request to the Alpha Advantage API to fetch stock prices
    for the specified dates. It extracts the closing prices for yesterday and the
    day before yesterday.

    Args:
        dates (tuple): A tuple containing two strings representing the dates
            for which to retrieve stock prices. The first element should be
            yesterday's date, and the second element should be the day before
            yesterday's date.

    Returns:
        tuple: A tuple containing two strings:
            - The closing price for yesterday.
            - The closing price for the day before yesterday.

    Raises:
        requests.exceptions.HTTPError: If the API request fails or returns an error.
    """
    try:
        r = requests.get(url=ALPHA_ADVANTAGE_API, params=ALPHA_PARAMETERS)
        r.raise_for_status()
        yesterday = r.json()["Time Series (Daily)"][dates[0]]["4. close"]
        day_before_yesterday = r.json()["Time Series (Daily)"][dates[1]]["4. close"]
        return yesterday, day_before_yesterday
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None, None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None, None


def get_news():
    """
    Retrieves news articles from the News API.

    Returns:
        list: A list of dictionaries, where each dictionary represents a news article.
            The dictionary contains the following keys:
            - COMPANY_NAME: A string representing the company name, with a symbol indicating the stock price change.
            - Headline: The headline of the news article.
            - Brief: A brief description of the news article.
            - URL: The URL of the news article.
            - Thumbnail: The URL of the thumbnail image for the news article.
        None, None: If an error occurs during the API request, the function returns `None, None`.

    Raises:
        requests.exceptions.HTTPError: If the API request returns an HTTP error.
        requests.exceptions.RequestException: If any other error occurs during the API request.
    """
    try:
        r = requests.get(url=NEWS_API, params=NEWS_PARAMETERS)
        r.raise_for_status()
        news_json = r.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return None, None
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return None, None
    else:
        news = []
        for i in range(int(NEWS_COUNT)):
            news.append(
                {
                    COMPANY_NAME: "🔺" + str(int(diff))
                    if diff >= 0
                    else "🔻" + str(int(diff) * -1),
                    "Headline": news_json["articles"][i]["title"],
                    "Brief": news_json["articles"][i]["description"],
                    "URL": news_json["articles"][i]["url"],
                    "Thumbnail": news_json["articles"][i]["urlToImage"],
                }
            )
        return news


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


stock_prices = get_stock_prices(get_dates())

# ? diff represents the percentual difference between the prices of yesterday & the day before yesterday.
diff = (
    (float(stock_prices[1]) - float(stock_prices[0])) / float(stock_prices[0])
) * 100

if diff > GET_NEWS_RISE_PERCENTAGE:
    company_news = get_news()

    message = f"{ALPHA_PARAMETERS['symbol']}'s daily news\n"

    for news in company_news:
        message += "\n"
        for key, value in news.items():
            message += f"{key}: {value}\n"

    send_email(message)
