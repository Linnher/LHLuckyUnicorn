# Version One of Yes / No Checker Function

# Function below this line:
def yesno(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("This is an invalid value. Please answer yes or no.")


# Main Routine below this line:
show_instructions = yesno("Have you played the game before? ")

print("You chose {}." .format(show_instructions))
print()
having_fun = yesno("Are you having fun? ")
print("You said {} to having fun.".format(having_fun))