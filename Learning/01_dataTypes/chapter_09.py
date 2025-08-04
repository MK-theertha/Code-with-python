# Define sets of essential and optional spices
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# Union: combine all unique elements from both sets
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

# Intersection: elements common to both sets
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# Difference: elements in essential_spices but not in optional_spices
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")

# Membership test: check if 'cloves' is in optional_spices
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")
