# ticket_checker.py

# Ask the user for their age
age = int(input("Enter your age: "))

# Store a Boolean value
is_adult = age >= 18

# Display the Boolean
print("Is adult:", is_adult)

# Decide the ticket price
if is_adult:
    print("Ticket Price: KSh 1000")
else:
    print("Ticket Price: KSh 500")
