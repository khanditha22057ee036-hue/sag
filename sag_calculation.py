# Sag Calculation of Overhead Transmission Line
# Electrical Engineering - Power Systems
# Formula: Sag = (w * L^2) / (8 * T)
#
# w = Weight of conductor per unit length (N/m)
# L = Span length (m)
# T = Tension in conductor (N)

def calculate_sag(weight, span, tension):
    """Calculate sag of an overhead transmission line."""
    sag = (weight * span ** 2) / (8 * tension)
    return sag


print("==========================================")
print("   OVERHEAD TRANSMISSION LINE SAG CALCULATOR")
print("==========================================")

# Input values
weight = float(input("Enter conductor weight (N/m): "))
span = float(input("Enter span length (m): "))
tension = float(input("Enter conductor tension (N): "))

# Calculate sag
sag = calculate_sag(weight, span, tension)

# Display result
print("\n---------- RESULT ----------")
print(f"Conductor Weight : {weight:.2f} N/m")
print(f"Span Length      : {span:.2f} m")
print(f"Conductor Tension: {tension:.2f} N")
print(f"Sag              : {sag:.3f} m")
print("----------------------------")
