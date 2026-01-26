#Weather Branch

import random

weather_events = [
    "Sunny",
    "Rain",
    "Heavy Rain",
    "Snow",
    "Blizzard",
    "Hail",
    "Ice Rain",
    "Thunderstorm",
    "Fog",
    "Windstorm"
]

random_weather = random.choice(weather_events)

print("Today's weather event:", random_weather)
