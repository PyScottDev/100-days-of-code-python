import smtplib
import datetime as dt
import random

my_email = "somebody@email.com"
password = "password"

now = dt.datetime.now()
year = now.year
day = now.day
month = now.month

weekday = now.weekday()

with open("day_32_smtp_email/quotes.txt") as file:
    lines = file.readlines()
myline = random.choice(lines)

# print(year)
# print(day)
print(day)
print(month)




if weekday == 2:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="somebody@email.com",
            msg=f"Subject: Hello from Python\n\nHi John\nI hope this message will mean something to you\n{myline}")




