# Version Two of Instructions Function

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


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game go here")
    print()
    return""


# Main Routine below this line:
played_before = yesno("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program Continues")