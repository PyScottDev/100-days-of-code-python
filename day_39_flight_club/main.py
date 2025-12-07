#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import os
from dotenv import load_dotenv
import requests
from datetime import datetime
from pprint import pprint
from flight_search import FlightSearch

flight_search = FlightSearch()

load_dotenv()
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")
SHEETY_BEARER = os.getenv("SHEETY_BEARER")

headers = {

    "Authorization": f"Bearer {SHEETY_BEARER}",
    "Content-Type": "application/json"

}

response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
response.raise_for_status()
data = response.json()

pprint(data)

sheet_data = data["prices"]
print(sheet_data)

for row in sheet_data:
    if row["iataCode"] == ""  or row["iataCode"] == None:
       iataCode = flight_search.get_iata_code(row["city"])
       row["iataCode"] = iataCode
print(sheet_data) 