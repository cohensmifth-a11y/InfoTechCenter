# =========================
# Weather Branch Simulation
# =========================
# This program simulates a car system that:
# 1. Detects random weather
# 2. Limits driving speed based on safety
# 3. Calculates travel time for a trip
# 4. Decides whether the driver must leave earlier

import random  # Used to randomly select weather and temperature

# -------------------------
# Trip Configuration
# -------------------------
# Total distance to the destination (miles)
distance_miles = 30

# Maximum amount of time allowed to reach the destination (minutes)
time_limit_minutes = 30

# -------------------------
# Weather Database
# -------------------------
# Each weather type contains:
# - temp: realistic temperature range (°F)
# - intensity: description of road/visibility conditions
# - max_speed: safe driving speed limit for that weather (mph)
weather_events = {
    "Sunny": {
        "temp": (70, 100),
        "intensity": "Clear",
        "max_speed": 70
    },
    "Rain": {
        "temp": (45, 75),
        "intensity": "Wet roads",
        "max_speed": 55
    },
    "Heavy Rain": {
        "temp": (50, 80),
        "intensity": "Poor visibility",
        "max_speed": 45
    },
    "Snow": {
        "temp": (10, 32),
        "intensity": "Slippery roads",
        "max_speed": 35
    },
    "Blizzard": {
        "temp": (-10, 25),
        "intensity": "Whiteout",
        "max_speed": 20
    },
    "Hail": {
        "temp": (30, 70),
        "intensity": "Impact risk",
        "max_speed": 25
    },
    "Ice Rain": {
        "temp": (28, 34),
        "intensity": "Black ice",
        "max_speed": 15
    },
    "Thunderstorm": {
        "temp": (60, 90),
        "intensity": "Severe storm",
        "max_speed": 40
    },
    "Fog": {
        "temp": (35, 65),
        "intensity": "Low visibility",
        "max_speed": 30
    },
    "Windstorm": {
        "temp": (40, 75),
        "intensity": "Strong crosswinds",
        "max_speed": 50
    }
}

# -------------------------
# Weather Selection
# -------------------------
# Randomly choose one weather event from the dictionary
event = random.choice(list(weather_events.keys()))

# Retrieve the data associated with the chosen weather
data = weather_events[event]

# Randomly generate a temperature within the weather's range
temperature = random.randint(*data["temp"])

# Get the maximum safe speed for the selected weather
max_speed = data["max_speed"]

# -------------------------
# Travel Time Calculation
# -------------------------
# Convert travel time from hours to minutes
# Formula: time = distance / speed
travel_time_hours = distance_miles / max_speed
travel_time_minutes = travel_time_hours * 60

# -------------------------
# Car System Output
# -------------------------
# Simulate a car infotainment / safety system message
print("🚗 Car System Online")
print("🌦️ Checking weather conditions...")
print(f"Weather detected: {event}")
print(f"Temperature: {temperature}°F")
print(f"Road condition: {data['intensity']}")
print(f"🚘 Max safe speed: {max_speed} mph")

# -------------------------
# Trip Analysis Output
# -------------------------
print("\n🧭 Trip Analysis")
print(f"Distance to destination: {distance_miles} miles")
print(f"Time available: {time_limit_minutes} minutes")
print(f"Estimated travel time: {travel_time_minutes:.1f} minutes")

# -------------------------
# Arrival Time Decision
# -------------------------
# Compare estimated travel time to the allowed time
if travel_time_minutes > time_limit_minutes:
    # Calculate how much extra time is needed
    extra_time = travel_time_minutes - time_limit_minutes

    # Warn the driver and simulate setting an earlier alarm
    print("\n⏰ ALERT: You will arrive late!")
    print(f"You need an extra {extra_time:.1f} minutes.")
    print("📱 Setting alarm earlier to compensate for weather conditions.")
else:
    # Inform the driver that no changes are needed
    print("\n✅ You will arrive on time.")
    print("No alarm adjustment needed.")

# -------------------------
# End of Program
# -------------------------
print("\nDrive safe! 🚙")
