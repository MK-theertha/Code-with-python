# Import modules for system info and precise number types
import sys
from fractions import Fraction
from decimal import Decimal

# Assign floating-point (float) values to temperature variables
ideal_temp = 95.5
current_temp = 95.49

# Print the ideal and current temperatures
print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")

# Print the difference between the two temperatures
print(f"Difference temp { ideal_temp - current_temp }")


# Print system-level information about float data type
print(sys.float_info)

