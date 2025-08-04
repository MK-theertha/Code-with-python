# List of staff members with their ages
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

# Loop through each staff member
for name, age in staff:
    # Check if the staff member is 18 or younger
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break  # Stop checking further once someone is eligible
else:
    # This will run ONLY if the for loop completes without hitting 'break'
    print(f"No one is eligible to manage the staff")

# Output:
# Amit is eligible to manage the staff