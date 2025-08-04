# Assigning string values to variables
chai_type = "Ginger chai"
customer_name = "Priya"

# Using f-string to format output
print(f"Order for {customer_name} : {chai_type} please !")

# A new string describing the chai
chai_description = "Aromatic and Bold"

# String slicing
print(f"First word: {chai_description[:8]}")   # Slices from index 0 to 7 (first word "Aromatic")
print(f"Last word: {chai_description[12:]}")   # Slices from index 12 to end ("Bold")
print(f"Reversed description: {chai_description[::-1]}")  # Reverses the string

# Working with Unicode and encoding
label_text = "Chai Spécial"  # Contains a special character (é)
ecoded_label = label_text.encode("utf-8")      # Encode string to bytes using UTF-8
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {ecoded_label}")        # Prints byte representation
decoded_label = ecoded_label.decode("utf-8")   # Decode back to string
print(f"Decoded label: {decoded_label}")
