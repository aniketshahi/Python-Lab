# Getting user input for different data types
user_input_int = int(input("Enter an integer: "))
user_input_float = float(input("Enter a float: "))
user_input_str = input("Enter a string: ")
user_input_bool_str = input("Enter True or False for boolean: ")

# Converting the string input to a boolean
user_input_bool = user_input_bool_str.lower() == 'true'

# Displaying the entered values and their types
print(f"Entered integer: {user_input_int}, Type: {type(user_input_int)}")
print(f"Entered float: {user_input_float}, Type: {type(user_input_float)}")
print(f"Entered string: {user_input_str}, Type: {type(user_input_str)}")
print(f"Entered boolean: {user_input_bool}, Type: {type(user_input_bool)}")
