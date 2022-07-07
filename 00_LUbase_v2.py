# Base component for the game Lucky Unicorn
# Version Two - Inserting the How Much? Component

# Author - Linn Herzig
# LH 2022


# Import libraries below this line:

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


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10!"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))

            # If the amount is too low / too high output:
            if low < response <= high:
               return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine below this line:
played_before = yesno("Have you played the game before? ")

if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}.".format(how_much))
