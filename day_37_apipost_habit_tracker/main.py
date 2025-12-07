import requests
from datetime import datetime

today = datetime.now()
today_str = today.strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "pyscottdev"
TOKEN = "hjkhjudh"

user_param = {

    "token": "hjkhjudh",
    "username": "pyscottdev",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {

    "id": "graph1",
    "name": "Coding Graph",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai",

}

headers = {

    "X-USER-TOKEN": TOKEN,

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

pixel_param = {

    "date": today_str,
    "quantity": "60",

}

response = requests.post(url=pixel_endpoint, json=pixel_param, headers=headers)
print(response.text)