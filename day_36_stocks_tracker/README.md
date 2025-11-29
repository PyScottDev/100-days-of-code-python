# Project Title: Stock Alert and News App

This script tracks the stock data of Nvidia and compares yesterday's closing price with that of the previous day.  If there is a change of more than 3%, a message is sent via WhatsApp that includes three recent stories on either Nvidia or AI.

## How it works

The script starts by retrieving data from Alpha Vantage on stock prices for Nvidia.  This is filtered and then a comparison is made between the two previous days' closing prices.  If that percentage difference is more than 3%, a request is put in to NewsAPI for stories connected to NVidia and AI.  From the filtered data, a message is composed, which is in turn passed on to Twilio
to be sent out as a WhatsApp message.

## Packages Used
- requests
- python-dotenv
- twilio
- json 
- os 

## APIs Used
- Alpha Vantage 
- NewsAPI 
- Twilio

## Folder Contents
- main.py
- .env (not committed)
- JSON test file
- READAME.md

## What I learned

This has been a fun project and has been a proper test in making API requests and then filtering the data that is received.  I decided to spend longer on this project as many of the features and logic are relevant for future projects that I wish to pursue.
