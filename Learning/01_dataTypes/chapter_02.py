# Create an empty set and assign it to the variable 'spice_mix'
spice_mix = set()

# Print the memory ID of the set object
print(f"Initial spice mix id: {id(spice_mix)}")

# Print the current content of the set (which is empty at this point)
print(f"Initial spice mix content: {spice_mix}")

# Add elements to the set (sets are mutable, so the same object is modified)
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")

# Print the updated content of the set
print(f"Updated spice mix content: {spice_mix}")

# Print the memory ID again to confirm it's the same object
print(f"After spice mix id: {id(spice_mix)}")

# Notes:
# spice_mix is a set.
# Sets are mutable—when modified, they retain the same memory identity.
# id() shows that even after adding elements, the set object remains the same.
