import requests

API_Key = "nix_live_UIrspxM63TbUwesJCZMylCIW0V7vikB5"
App_ID = "app_70df9409991744248e60f2cf"

GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 193
AGE = 49

nutEx_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

headers = {

    "x-app-id": App_ID,
    "x-app-key": API_Key,

}

nutEX_config = {

    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,


}   

response = requests.post(url=nutEx_endpoint, json=nutEX_config, headers=headers)
print(response.text)

result = response.json()
print(result)


