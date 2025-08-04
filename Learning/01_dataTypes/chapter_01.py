# Assign an integer value 2 to the variable 'sugar_amount'
sugar_amount = 2

# Print the initial value of sugar_amount
print(f"Initial sugar: {sugar_amount}")

# Reassign a new integer value 12 to the same variable
sugar_amount = 12

# Print the new value of sugar_amount after reassignment
print(f"Second Initial sugar: {sugar_amount}")

# Print the memory address (unique ID) of the integer object 2
print(f"ID of 2: {id(2)}")

# Print the memory address (unique ID) of the integer object 12
print(f"ID of 12: {id(12)}")

# Notes:
# sugar_amount is an integer.
# Integers are immutable—when reassigned, a new object is used.
# id() shows the memory identity of those immutable integer objects.