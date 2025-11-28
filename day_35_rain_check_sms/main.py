import requests
import smtplib

MY_EMAIL = "Your_email@email.com"
PASSWORD = "password"
#api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
APP_KEY = "604900665720a8ae743640ec15a4682d"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

MY_LAT = 53.4509
MY_LONG = -6.1501
parameters ={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": APP_KEY,
    "cnt": 4,

}

response = requests.get(url=OWM_ENDPOINT, params=parameters)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for entry in weather_data["list"]:
    weather_id = entry["weather"][0]["id"]
    if weather_id < 700:
         will_rain = True    

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="somebody@email.com",
            msg="Subject: Rain Alert!\n\nBring an umbrella"
        )