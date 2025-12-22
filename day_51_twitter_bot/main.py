import os
from dotenv import load_dotenv
import InternetSpeedTwitterBot

load_dotenv()  # reads .env in the current working directory

PROMISED_DOWN = 1000 
PROMISED_UP = 25    
TWITTER_EMAIL = os.getenv("TWITTER_EMAIL")
TWITTER_USERNAME = os.getenv("TWITTER_USERNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")

bot = InternetSpeedTwitterBot.InternetSpeedTwitterBot()
download_speed, upload_speed = bot.get_internet_speed()
print(download_speed)
print(upload_speed)
if float(download_speed) < PROMISED_DOWN:
    bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_USERNAME, TWITTER_PASSWORD, PROMISED_DOWN, download_speed)
