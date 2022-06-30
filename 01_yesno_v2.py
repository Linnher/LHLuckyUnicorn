# Version Two of Yes / No Checker

show_instructions = ""
while show_instructions.lower() != "xxx":

    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If the user inputs yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("Program Continues")

    # If the user inputs no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("Display Instructions")

    # If user inputs anything else, output 'This is an invalid value.'
    else:
        print("This is an invalid value. Please answer yes or no.")

    print("You chose {}.".format(show_instructions))
