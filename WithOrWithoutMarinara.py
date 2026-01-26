#Weather Branch

import random

# Trip details
distance_miles = 30
time_limit_minutes = 30

# Weather data with safe speed limits (mph)
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

# Calculate travel time
travel_time_hours = distance_miles / max_speed
travel_time_minutes = travel_time_hours * 60

# Car "conversation"
print("🚗 Car System Online")
print("🌦️ Checking weather conditions...")
print(f"Weather detected: {event}")
print(f"Temperature: {temperature}°F")
print(f"Road condition: {data['intensity']}")
print(f"🚘 Max safe speed: {max_speed} mph")

print("\n🧭 Trip Analysis")
print(f"Distance to destination: {distance_miles} miles")
print(f"Time available: {time_limit_minutes} minutes")
print(f"Estimated travel time: {travel_time_minutes:.1f} minutes")

if travel_time_minutes > time_limit_minutes:
    extra_time = travel_time_minutes - time_limit_minutes
    print("\n⏰ ALERT: You will arrive late!")
    print(f"You need an extra {extra_time:.1f} minutes.")
    print("📱 Setting alarm earlier to compensate for weather conditions.")
else:
    print("\n✅ You will arrive on time.")
    print("No alarm adjustment needed.")

print("\nDrive safe! 🚙")
