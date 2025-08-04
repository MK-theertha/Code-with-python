# Import the arrow library for better date/time handling
import arrow

# Get the current UTC time
brewing_time = arrow.utcnow()

# Convert the UTC time to a different timezone (Europe/Rome)
brewing_time.to("Europe/Rome")
# Note: This does not modify brewing_time unless reassigned
# You should do: brewing_time = brewing_time.to("Europe/Rome") if you want to store the converted time

# Import namedtuple from collections module
from collections import namedtuple

# Define a namedtuple called chaiProfile with two fields: flavor and aroma
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

# Example usage:
# profile = chaiProfile(flavor="bold", aroma="spicy")
# print(profile.flavor, profile.aroma)
