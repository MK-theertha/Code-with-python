# List of basic ingredients
ingredients = ["water", "milk", "black tea"]

# Add an ingredient using append()
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")

# Remove an ingredient using remove()
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

# Additional spice options and base chai ingredients
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# Extend chai_ingredients by adding items from spice_options
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

# Insert 'black tea' at index 2
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

# Remove and return the last item using pop()
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

# Reverse the list order
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")

# Sort the list alphabetically
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

# Working with numeric list
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")  # Find max value
print(f"Minimum sugar level: {min(sugar_levels)}")  # Find min value

# Concatenate two lists
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")

# Repeat a list multiple times
strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")

# Using bytearray for binary data manipulation
raw_spice_data = bytearray(b"CINNAMON")  # Create mutable byte array
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")  # Replace bytes
print(f"Bytes: {raw_spice_data}")
