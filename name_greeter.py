# name_greeter.py

# Ask the user to enter their full name
full_name = input("Please enter your full name: ")

# Split the name into separate words
name_parts = full_name.split()

# Check if the user entered two or more names
if len(name_parts) >= 2:
    print("Hello,", name_parts[0] + "!")
else:
    print("Please enter your full name (first and last name).")
