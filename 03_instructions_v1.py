# Version One of Instructions Function

# Function below this line:
def yesno(question):


def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game fo here")
    print()
    return""

# Main Routine below this line:
played_before = yesno("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program Continues")