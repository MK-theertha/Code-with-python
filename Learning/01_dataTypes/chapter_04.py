# Boolean and type conversion operations

# Boolean value representing whether the water is boiling
is_boiling = True  # Internally, True == 1 and False == 0

# Integer value representing how many times tea is stirred
stri_count = 5

# Adding an integer and a boolean: True is treated as 1 (upcasting to int)
total_actions = stri_count + is_boiling
print(f"Total actions: {total_actions}")
# Output will be 6, because 5 + True (which is 1) = 6

# Integer value 0 (falsy) representing no milk
milk_present = 0
print(f"Is there milk? {bool(milk_present)}")
# 0 is considered False when converted to boolean

# Two boolean values indicating conditions for serving tea
water_hot = True
tea_added = True

# Logical AND operation: both must be True to serve chai
can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}")

# Notes:
# - Booleans in Python are a subtype of integers: True == 1, False == 0.
# - When used in arithmetic, booleans are automatically upcast to integers.
# - The bool() function converts values to boolean (e.g., bool(0) → False, bool(1) → True).
# - Logical operators like `and`, `or`, `not` work with boolean expressions.
