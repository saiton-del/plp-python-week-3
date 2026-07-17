# bug_hunt.py

# BUG: Added the missing closing quotation mark to fix the SyntaxError.
print("Welcome to the Bug Hunt!")

name = input("What is your name? ")

# BUG: Replaced the text "nmae" with the variable name so it prints the user's name.
print("Nice to meet you,", name)

age = input("How old are you? ")

# BUG: Converted age to an integer before adding 1, then converted the result back to a string.
print("Next year you will be " + str(int(age) + 1))
