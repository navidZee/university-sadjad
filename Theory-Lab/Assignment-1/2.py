import random


def bold(string):
    """
    This function returns a bolded string.
    """
    return "\033[1m" + string + "\033[0m"

runCount = 0
computerNumber = random.randint(1, 100)
print("I'm thinking of a number between 1 and 100. so, what try to guess it?")
userInput = int(input())

while userInput != computerNumber:
    runCount += 1

    if userInput > computerNumber:
        print("Too high")
        userInput = int(input("Guess again: "))
    elif userInput < computerNumber:
        print("Too low")
        userInput = int(input("Guess again: "))


message = "Hey!!!, You found it. \n\rIt took you " + str(runCount) + " tries."
print(bold(message))