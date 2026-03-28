# Ohm's Law Program

# Input from user
voltage = float(input("Enter Voltage (V): "))
resistance = float(input("Enter Resistance (R): "))

# Avoid division by zero
if resistance == 0:
    print("Resistance cannot be zero!")
else:
    current = voltage / resistance
    print("Current (I) =", current, "Amperes")

    # Check nature of current
    if current < 0.5:
        print("Low current")
    elif 0.5 <= current <= 2:
        print("Normal current")
    else:
        print("High current")
