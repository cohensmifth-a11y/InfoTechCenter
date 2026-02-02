#Gasoline Branch

import random
# -----------------------------
# Gas level (PERCENT BASED)
# -----------------------------
gas_level_percent = random.randint(0, 100)
TANK_CAPACITY = 16  # gallons
MPG = 25

current_gas_gallons = (gas_level_percent / 100) * TANK_CAPACITY
max_distance = current_gas_gallons * MPG

# Fake dashboard alarm
low_fuel_alarm = False

print(f"Gas level: {gas_level_percent}%")
print(f"Gas in tank: {current_gas_gallons:.2f} gallons")
print(f"Max distance you can drive: {max_distance:.1f} miles")

# Quarter tank warning
if gas_level_percent < 25:
    low_fuel_alarm = True
    print("⚠️ WARNING: Gas level below quarter tank!")
else:
    print("✅ Gas level is sufficient.")

# -----------------------------
# Fake gas stations
# -----------------------------
gas_stations = [
    {
        "name": "Shell",
        "distance": random.randint(2, 20),
        "price": round(random.uniform(3.20, 4.50), 2),
        "open": random.choice([True, False]),
        "slurpees": random.choice([True, False]),
        "snacks": random.choice([True, False])
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

print("\nAvailable gas stations:")
for s in gas_stations:
    print(
        f"- {s['name']}: {s['distance']} miles | "
        f"${s['price']}/gal | "
        f"{'OPEN' if s['open'] else 'CLOSED'} | "
        f"Slurpees: {'YES' if s['slurpees'] else 'NO'} | "
        f"Snacks: {'YES' if s['snacks'] else 'NO'}"
    )

# -----------------------------
# Helper functions
# -----------------------------
def can_reach(station):
    return station["distance"] <= max_distance

def is_usable(station):
    return station["open"] and can_reach(station)

# -----------------------------
# Analysis
# -----------------------------
usable_stations = [s for s in gas_stations if is_usable(s)]

print("\n--- Analysis ---")

if usable_stations:
    closest_station = min(usable_stations, key=lambda s: s["distance"])
    cheapest_station = min(usable_stations, key=lambda s: s["price"])

    print(f"Closest OPEN station: {closest_station['name']} ({closest_station['distance']} miles)")
    print(f"Cheapest OPEN station: {cheapest_station['name']} (${cheapest_station['price']}/gal)")

    # Fun extras
    if cheapest_station["slurpees"] or cheapest_station["snacks"]:
        print("🍿 Bonus items available at cheapest station!")
else:
    low_fuel_alarm = True
    print("🚨 NO OPEN & REACHABLE GAS STATIONS!")

# -----------------------------
# Dashboard alarm status
# -----------------------------
print("\n--- Dashboard Status ---")
if low_fuel_alarm:
    print("🔔 LOW FUEL ALARM: ON")
else:
    print("🔕 Low fuel alarm: OFF")

closest_station = min(gas_stations, key=lambda s: s["distance"])
cheapest_station = min(gas_stations, key=lambda s: s["price"])

print("\n--- Analysis ---")

print(f"Closest station: {closest_station['name']} ({closest_station['distance']} miles)")
print("Reachable?", "YES ✅" if can_reach(closest_station) else "NO ❌")

print(f"\nCheapest station: {cheapest_station['name']} (${cheapest_station['price']}/gal)")
print("Reachable?", "YES ✅" if can_reach(cheapest_station) else "NO ❌")

# -----------------------------
# Best reachable option
# -----------------------------
reachable_stations = [s for s in gas_stations if can_reach(s)]

if reachable_stations:
    best_choice = min(reachable_stations, key=lambda s: s["price"])
    print(f"\n🏁 Best reachable station: {best_choice['name']} "
          f"({best_choice['distance']} miles, ${best_choice['price']}/gal)")
else:
    print("\n🚨 EMERGENCY: No reachable gas stations!")
