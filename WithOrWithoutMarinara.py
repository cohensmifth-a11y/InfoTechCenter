
#BetaTestDev

#Welcome Branch

#Libraries Imported Here
import sys          # Allows us to write to the terminal without a newline
import time         # Allows us to add delays (sleep)

# ANSI color codes for terminal text
RESET = "\033[0m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BOLD = "\033[1m"

# Display welcome messages
print(f"\n{CYAN}{BOLD}Welcome Branch - Developer: Cohen Smith{RESET}")
print(f"\n{CYAN}Welcome to InfoTechCenter V.1.0{RESET}")

# Initialize counters
x = 0               # Controls how long the boot sequence runs
ellipsis = 0        # Controls how many dots appear in the animation

# Boot animation loop
while x != 20:
    x += 1          # Increase loop counter

    # Create the boot message with animated dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1

    # Rewrite the same terminal line instead of printing a new one
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dots after three dots
    if ellipsis == 4:
        ellipsis = 0

    # Final message after boot completes
    if x == 20:
        print(f"\n{GREEN}{BOLD}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")
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

#Gasoline Branch

import random  # Used to generate fake/random values for the simulation

# =====================================================
# GAS LEVEL (PERCENT-BASED SYSTEM)
# =====================================================

# Generate a fake gas level as a percentage (0–100%)
gas_level_percent = random.randint(0, 100)

# Define car constants
TANK_CAPACITY = 16   # Total fuel tank size in gallons
MPG = 25             # Miles per gallon efficiency

# Convert gas percentage into actual gallons
current_gas_gallons = (gas_level_percent / 100) * TANK_CAPACITY

# Calculate how far the car can drive with current fuel
max_distance = current_gas_gallons * MPG

# Fake dashboard alarm (starts OFF)
low_fuel_alarm = False

# Display fuel information
print(f"Gas level: {gas_level_percent}%")
print(f"Gas in tank: {current_gas_gallons:.2f} gallons")
print(f"Max distance you can drive: {max_distance:.1f} miles")

# Check if gas is below a quarter tank (25%)
if gas_level_percent < 25:
    low_fuel_alarm = True  # Turn alarm ON
    print("⚠️ WARNING: Gas level below quarter tank!")
else:
    print("✅ Gas level is sufficient.")

# =====================================================
# GAS STATION DATA (FAKE / RANDOMIZED)
# =====================================================

# Create a list of gas stations with random properties
gas_stations = [
    {
        "name": "Shell",
        "distance": random.randint(2, 20),  # Distance from car (miles)
        "price": round(random.uniform(3.20, 4.50), 2),  # Gas price per gallon
        "open": random.choice([True, False]),  # Whether station is open
        "slurpees": random.choice([True, False]),  # Slurpees available?
        "snacks": random.choice([True, False])  # Snacks available?
    },
    {
        "name": "Exxon",
        "distance": random.randint(2, 20),
        "price": round(random.uniform(3.20, 4.50), 2),
        "open": random.choice([True, False]),
        "slurpees": random.choice([True, False]),
        "snacks": random.choice([True, False])
    },
    {
        "name": "BP",
        "distance": random.randint(2, 20),
        "price": round(random.uniform(3.20, 4.50), 2),
        "open": random.choice([True, False]),
        "slurpees": random.choice([True, False]),
        "snacks": random.choice([True, False])
    },
    {
        "name": "Chevron",
        "distance": random.randint(2, 20),
        "price": round(random.uniform(3.20, 4.50), 2),
        "open": random.choice([True, False]),
        "slurpees": random.choice([True, False]),
        "snacks": random.choice([True, False])
    }
]

# Display all gas stations and their details
print("\nAvailable gas stations:")
for s in gas_stations:
    print(
        f"- {s['name']}: {s['distance']} miles | "
        f"${s['price']}/gal | "
        f"{'OPEN' if s['open'] else 'CLOSED'} | "
        f"Slurpees: {'YES' if s['slurpees'] else 'NO'} | "
        f"Snacks: {'YES' if s['snacks'] else 'NO'}"
    )

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def can_reach(station):
    """
    Returns True if the car has enough fuel
    to reach the given gas station.
    """
    return station["distance"] <= max_distance

def is_usable(station):
    """
    Returns True if the station is BOTH:
    - Open
    - Reachable with current fuel
    """
    return station["open"] and can_reach(station)

# =====================================================
# STATION ANALYSIS
# =====================================================

# Filter stations to only those that are open AND reachable
usable_stations = [s for s in gas_stations if is_usable(s)]

print("\n--- Analysis ---")

if usable_stations:
    # Find closest usable station
    closest_station = min(usable_stations, key=lambda s: s["distance"])

    # Find cheapest usable station
    cheapest_station = min(usable_stations, key=lambda s: s["price"])

    print(f"Closest OPEN station: {closest_station['name']} ({closest_station['distance']} miles)")
    print(f"Cheapest OPEN station: {cheapest_station['name']} (${cheapest_station['price']}/gal)")

    # Extra fun logic: check for snacks or slurpees
    if cheapest_station["slurpees"] or cheapest_station["snacks"]:
        print("🍿 Bonus items available at cheapest station!")
else:
    # No stations can be reached → emergency situation
    low_fuel_alarm = True
    print("🚨 NO OPEN & REACHABLE GAS STATIONS!")

# =====================================================
# DASHBOARD STATUS
# =====================================================

print("\n--- Dashboard Status ---")

# Final alarm state
if low_fuel_alarm:
    print("🔔 LOW FUEL ALARM: ON")
else:
    print("🔕 Low fuel alarm: OFF")