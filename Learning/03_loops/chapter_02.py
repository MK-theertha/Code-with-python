# List of available chai menu items
menu = ["Green", "Lemon", "Spiced", "Mint"]

# Loop through the menu with both index and item using enumerate()
# 'start=1' makes the index begin from 1 instead of 0
for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")
