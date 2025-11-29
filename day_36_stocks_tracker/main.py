import requests
import json
from twilio.rest import Client
from dotenv import load_dotenv
import os

# ----------------------- LOAD SECRETS -------------------
load_dotenv()
NEWSAPI_Key = os.getenv("NEWSAPI_Key")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
my_number = os.getenv("my_number")
ALPHA_KEY = os.getenv("ALPHA_KEY")

# ----------------------- CONSTANTS ----------------------
STOCK = "NVDA"
COMPANY_NAME = "Nvidia"
ALPHA_EP = "https://www.alphavantage.co/query"
NWSAPI_EP = "https://newsapi.org/v2/everything?"
twilio_whatsapp = "whatsapp:+14155238886"    

# ----------------------- FUNCTIONS ----------------------  
def get_stock_prices():
    alpha_parameters = {

        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_KEY,

    }

    alpha_response = requests.get(ALPHA_EP, params=alpha_parameters)
    alpha_response.raise_for_status()
    alpha_data = alpha_response.json()

    # with open("day_36_stocks_tracker/alpha_data.json") as f:  # For testing without calling the Alpha API
    #     alpha_data = json.load(f)
    return alpha_data


def get_percentage(data):
    daily_list = []
    daily_data = data["Time Series (Daily)"]
    days = list(daily_data.keys())
    yesterday = days[0]
    day_before = days[1]

    yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
    day_before_close = float(data["Time Series (Daily)"][day_before]["4. close"])

    percentage_change = (yesterday_close - day_before_close) / day_before_close * 100
    return percentage_change

def get_news():
    newsapi_parameters ={

        "q": "Nvidia AND AI",
        "language": "en",
        "apiKey": NEWSAPI_Key

    }

    news_response = requests.get(NWSAPI_EP, params=newsapi_parameters)
    news_response.raise_for_status()

    news_data = news_response.json()

    three_articles = news_data["articles"][:3]
   
    result = []
    for article in three_articles:
        entry = {

            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
            "image_url": article["urlToImage"],

        }
        result.append(entry)
    return result   

def create_message(result, percent_change):
    arrow = "🔺" if percent_change > 0 else "🔻"
    message_body = (
        f"*{COMPANY_NAME} stock {abs(percent_change):.1f}%{arrow}*\n\n"
        "Here's the most recent news on Nvidia and AI\n\n"
        f"*{result[0]['title']}*\n{result[0]['description']}\nFind more at {result[0]['url']}\n\n"
        f"*{result[1]['title']}*\n{result[1]['description']}\nFind more at {result[1]['url']}\n\n"
        f"*{result[2]['title']}*\n{result[2]['description']}\nFind more at {result[2]['url']}\n\n"

    )
    news_image = result[0]["image_url"]
    return message_body, news_image

def send_message(body, image):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        from_=twilio_whatsapp,
        to=my_number,
        body=body,
        media_url=[image]
    )

    print("Message SID:", message.sid)

# ----------------------- RUN PROGRAM ----------------------
alpha_data = get_stock_prices()
percent_change = get_percentage(alpha_data)
if abs(percent_change) > 1:
    result = get_news()
    message_body, news_image = create_message(result, percent_change)
    send_message(message_body, news_image)

