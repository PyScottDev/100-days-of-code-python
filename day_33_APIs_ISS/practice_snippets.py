# import requests

# url = "http://api.open-notify.org/iss-now.json"

# response = requests.get(url)
# response.raise_for_status()

# data = response.json()

# print(data["iss_position"]["latitude"])
# print(data["iss_position"]["longitude"])
# print(data)
# print(response.status_code)

# import requests

# url = "https://api.kanye.rest"

# response = requests.get(url)
# response.raise_for_status()

# data = response.json()

# quote = data["quote"]

# print(quote)

import requests
from datetime import datetime as dt
MY_LAT = 53.4509
MY_LON = 6.1501

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0,

}

time_now = dt.now()
current_hour = time_now.hour



url = "https://api.sunrise-sunset.org/json"

response = requests.get(url, params=parameters)
response.raise_for_status()

data = response.json()

#print(data)
sunset = data["results"]["sunset"]
parts = sunset.split("T")
print(parts)

time_section = parts[1].split(":")
print(time_section)

sunset_hour = time_section[0]
print(sunset_hour)

####Sunrise#####
sunrise = data["results"]["sunrise"]
parts = sunrise.split("T")
print(parts)

time_section = parts[1].split(":")
print(time_section)

sunrise_hour = time_section[0]
print(sunrise_hour)


sunrise_hour = int(sunrise_hour)
sunset_hour = int(sunset_hour)

if current_hour >= sunset_hour or current_hour <= sunrise_hour:
    print("It's dark")
else:
    print("It's light")