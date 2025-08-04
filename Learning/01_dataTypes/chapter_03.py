# Integer operations in a tea preparation context

# Assign integer values to variables representing grams of ingredients
black_tea_grams = 14
ginger_grams = 3

# Add two integers
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}")

# Subtract two integers
remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}")

# Divide two integers to get a float result
milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}")

# Integer division (floor division) to get whole number result
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

# Modulus operation to find the remainder
total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}")

# Exponentiation (power operation)
base_flavor_strength = 2
scale_factor = 3
powerful_falvour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerful_falvour}")
# 2 ** 3 = 2 * 2 * 2 = 8

# Use of underscore for readability in large numbers
total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}")

# Notes:
# All variables here use the integer (int) data type, except where division gives a float.
# Operations shown: addition (+), subtraction (-), division (/), floor division (//), modulus (%), exponentiation (**).
# Underscores in numbers (like 1_000_000_000) improve readability without affecting value.
# Division (/) returns a float even if both operands are integers.
