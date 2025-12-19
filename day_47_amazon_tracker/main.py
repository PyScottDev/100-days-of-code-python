from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

header ={
        
        "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

URL_CLONE = "https://appbrewery.github.io/instant_pot/"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(URL, headers=header)
response.raise_for_status()

amazon_page = response.text
soup = BeautifulSoup(amazon_page, "html.parser")

whole_tag = soup.find("span", class_="a-price-whole")
whole = float(whole_tag.get_text())
print(whole)

decimal_tag = soup.find("span", class_="a-price-fraction")
decimal = float(decimal_tag.get_text()) / 100
print(decimal)
price = whole + decimal
print(price)


if price < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject: Price Alert\n\nGet on to Amazon now and buy that Instant Pot!")