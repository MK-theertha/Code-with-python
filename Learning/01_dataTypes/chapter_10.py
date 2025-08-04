# Create a dictionary using keyword arguments
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

# Create an empty dictionary and add key-value pairs one by one
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

# Accessing values using keys
print(f"Recipe base: {chai_recipe['base']}")
print(f"Recipe: {chai_recipe}")

# Delete a specific key-value pair using del
del chai_recipe["liquid"]
print(f"Recipe after deletion: {chai_recipe}")

# Check if a key exists in the dictionary
print(f"Is sugar in the order? {'sugar' in chai_order}")

# Reassign chai_order with new values
chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# You can inspect keys, values, and items using:
# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

# Remove and return the last inserted key-value pair (since Python 3.7)
last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

# Add multiple key-value pairs at once using update()
extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

# Show updated dictionary after adding new spices
print(f"Updated chai recipe: {chai_recipe}")

# Safely get a value using get(); returns "NO Note" if key doesn't exist
customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")

# -----------------------------
# Summary Notes:
# - Dictionaries (dict) store key-value pairs.
# - You can create them using dict() or {}.
# - Keys must be unique and immutable (e.g., strings, numbers).
# - Access values with dict[key] or safely with dict.get(key, default).
# - Use update() to merge another dictionary.
# - popitem() removes the last inserted item.
# - del removes a specific key from the dictionary.
# - Use 'in' to check if a key exists.
