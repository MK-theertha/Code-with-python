# Global variable defined
chai_type = "ginger"

# Define a function that represents updating a chai order
def update_order():
    # This variable is local to update_order and shadows the global one
    chai_type = "Elaichi"

    # Define a nested function that represents the kitchen making a change
    def kitchen():
        # nonlocal tells Python to use the chai_type from update_order(), not a new one
        nonlocal chai_type
        # Modify the chai_type variable from the outer function (update_order)
        chai_type = "Kesar"

    # Call the kitchen function, which modifies chai_type from "Elaichi" to "Kesar"
    kitchen()

    # Print the updated value of chai_type after kitchen() runs
    print("After kitchen update", chai_type)

# Call the update_order function to run the logic
update_order()
