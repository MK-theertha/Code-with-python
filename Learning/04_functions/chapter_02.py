# A pure function: always gives the same output for the same input, no side effects
def pure_chai(cups):
    return cups * 10  # Each cup assumed to cost 10 units

# Global variable (used below in an impure function – not recommended)
total_chai = 0

# An impure function: modifies the external (global) variable total_chai
def impure_chai(cups):
    global total_chai  # Refers to the global variable instead of creating a local one
    total_chai += cups  # Side effect: changes global state

# Recursive function to simulate pouring chai cups one by one
def pour_chai(n):
    print(n)  # Print the current cup number
    if n == 0:
        return "All cups poured"  # Base case: when no cups left
    return pour_chai(n - 1)  # Recursive call with one less cup

# Call the recursive function with 3 cups to pour
print(pour_chai(3))  
# Output:
# 3
# 2
# 1
# 0
# All cups poured

# List of different types of chai
chai_types = ["light", "kadak", "ginger", "kadak"]

# Filter out "kadak" chai from the list using a lambda function
strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))

# Print the filtered list (chai types that are not "kadak")
print(strong_chai)
# Output: ['light', 'ginger']
