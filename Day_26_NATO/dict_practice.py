# # # music_library = {
# # #     "rock": ["Queen", "Nirvana", "Foo Fighters"],
# # #     "pop": ["Taylor Swift", "Dua Lipa"],
# # #     "electronic": ["Daft Punk", "Flume"]
# # # }


# # # music_list = []

# # # for genre, artist in music_library.items():
# # #     new_entry = {"genre": genre, "artists": artist}
# # #     music_list.append(new_entry)

# # # print(music_list)

# # scores = {
# #     "Alice": 82,
# #     "Ben": 59,
# #     "Cara": 91,
# #     "Dean": 45,
# #     "Ella": 73,
# # }

# # passed = {name: score for name, score in scores.items() if score >= 60}
# # print(passed)

# temperatures_c = [0, 12, 17, 21, 30]

# temp_f = {temp: (temp * 9/5 +32) for temp in temperatures_c}

# print(temp_f)

weather_data = {
    "Mon": {"temp": 12, "condition": "sunny"},
    "Tue": {"temp": 14, "condition": "cloudy"},
    "Wed": {"temp": 17, "condition": "rain"},
    "Thu": {"temp": 21, "condition": "sunny"},
    "Fri": {"temp": 19, "condition": "windy"},
}

warm_days = {day: weather for day, weather in weather_data.items() if weather["temp"] >= 18}

print(warm_days)

