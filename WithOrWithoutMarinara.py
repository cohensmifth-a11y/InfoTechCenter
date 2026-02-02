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
