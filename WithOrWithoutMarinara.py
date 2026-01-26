#Weather Branch

import random

# Weather data with safety speed limits (mph)
weather_events = {
    "Sunny": {"temp": (70, 100), "intensity": "Clear", "max_speed": 70},
    "Rain": {"temp": (45, 75), "intensity": "Wet roads", "max_speed": 55},
    "Heavy Rain": {"temp": (50, 80), "intensity": "Poor visibility", "max_speed": 45},
    "Snow": {"temp": (10, 32), "intensity": "Slippery roads", "max_speed": 35},
    "Blizzard": {"temp": (-10, 25), "intensity": "Whiteout", "max_speed": 20},
    "Hail": {"temp": (30, 70), "intensity": "Impact risk", "max_speed": 25},
    "Ice Rain": {"temp": (28, 34), "intensity": "Black ice", "max_speed": 15},
    "Thunderstorm": {"temp": (60, 90), "intensity": "Severe storm", "max_speed": 40},
    "Fog": {"temp": (35, 65), "intensity": "Low visibility", "max_speed": 30},
    "Windstorm": {"temp": (40, 75), "intensity": "Strong crosswinds", "max_speed": 50}
}

# Pick random weather
event = random.choice(list(weather_events.keys()))
data = weather_events[event]

temperature = random.randint(*data["temp"])
max_speed = data["max_speed"]

# Car "conversation"
print("🚗 Car System Online")
print("🌦️ Checking weather conditions...")
print(f"Weather detected: {event}")
print(f"Temperature: {temperature}°F")
print(f"Road condition: {data['intensity']}")

if max_speed < 60:
    print("⚠️ Warning: Unsafe driving conditions detected.")
else:
    print("✅ Conditions are safe for normal driving.")

print(f"🚘 Recommended maximum speed: {max_speed} mph")
print("Drive safe!")
