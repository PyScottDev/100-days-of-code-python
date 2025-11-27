import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 53.4509 # Your latitude
MY_LONG = -6.1501 # Your longitude
MY_EMAIL = "somebody@email.com"
MY_PASSWORD ="password"

#Is position within +5 or -5 degrees of the ISS.
def iss_overhead():
    latitude = False
    longitude = False
    lss_close = False
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (
        (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5)
        and
        (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5)
    )
    ## Old version now cleaned up
    # if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5):
    #     latitude  = True
    # if (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5):
    #     longitude  = True
    # if latitude == True and longitude == True:
    #     iss_close = True
    # return iss_close
    
#Calculate if it is datk
def is_dark():
    dark_yes = False
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour
    return current_hour >= sunset or current_hour <= sunrise
    # if current_hour >= sunset or current_hour >= sunrise:  ## Old version, now cleaned up and more compact
    #     return dark_yes


## Email notification
def email_alert():
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="another@email.com",
                msg="Subject: ISS Alert\n\nIf you look up now, you might see it. No idea about the weather, however, as I didn't have that API")


while True:
    if iss_overhead() and is_dark():
        email_alert()
    time.sleep(60)


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



