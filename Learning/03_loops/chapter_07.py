# --- Example 1: Using walrus operator to assign and check remainder ---

value = 13

# Assign remainder and check it in the same line
if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}")
# If remainder is non-zero, it's not divisible by 5

# --- Example 2: Requesting chai cup size with walrus operator ---
# Uncomment to use interactively:
# available_sizes = ["small", "medium", "large"]
# 
# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")

# --- Example 3: Keep asking for flavor until user enters a valid one ---

flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

# Keep prompting until a valid flavor is entered
while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

# Once valid input is entered
print(f"You choose {flavor} chai")
