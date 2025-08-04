# List of customer names
names = ["Hitesh", "Meera", "Sam", "Ali"]

# Corresponding list of bill amounts
bills = [50, 70, 100, 55]

# Loop through both lists simultaneously using zip()
for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
