#Gasoline Branch

# Tank details
tank_capacity = 16  # gallons
current_gas = 3.5   # gallons (fake value)

quarter_tank = tank_capacity * 0.25

print(f"Current gas: {current_gas:.1f} gallons")

if current_gas < quarter_tank:
    print("⚠️ WARNING: Low fuel! Find a gas station.")
else:
    print("✅ Fuel level is OK.")
