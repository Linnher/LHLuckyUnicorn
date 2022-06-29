# Ask the user if they have played before
show_instructions = input("Have you played this game before? ")

# If the user inputs yes, output 'program continues'
if show_instructions.lower() == "yes":
    print("Program Continues")

elif show_instructions.lower() == "y":
    print("Program Continues")

# If the user inputs no, output 'display instructions'
elif show_instructions.lower() == "no":
    print("Display Instructions")

elif show_instructions.lower() == "n":
    print("Display Instructions")

# If user inputs anything else, output 'This is an invalid value.'
else:
    print("This is an invalid value. Please answer yes or no.")

print("You chose {}.".format(show_instructions))



