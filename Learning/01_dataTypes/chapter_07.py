# Define a tuple containing masala spices
masala_spices = ("cardamom", "cloves", "cinnamon")

# Tuple unpacking: assign each element of the tuple to individual variables
(spice1, spice2, spice3) = masala_spices

# Print the unpacked values
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

# Assign integer values representing spice ratios
ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# Swap the values using multiple assignment
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# Membership test: check if "cinnamon" is in the tuple
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")
