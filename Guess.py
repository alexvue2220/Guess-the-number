import random


## Prompt user.
print("Hello!!")
print("Do you want to play a guessing number game?")
print("yes or no")

userinput = input (': ')[0].lower()

## Ensure yes or no.
while userinput not in ["y","n"]:
    print("Please answer yes or no")
    userinput = input (': ')[0].lower()

## End simulator.
if userinput == "n":
    exit()

## have user guess a number.
guess_number = int(input("Guess a number from 1 to 1,000: "))

real_number = random.randint(1,101)

## repeat game until number is guessed.
while True:
    ## Reprompting the user.
    if guess_number == real_number:
        print("You guessed right")
        userinput = input("Want to play again? ")

        if userinput == "n":
            exit()
        else:
            guess_number = int(input("Guess again: "))
            real_number = random.randint(1,101)

    ## stating whether high or low.
    if guess_number > real_number:
        print("Your number is high")
        guess_number = int(input("Guess again: "))

    else:
        print("Your number is low")
        guess_number = int(input("Guess again: "))