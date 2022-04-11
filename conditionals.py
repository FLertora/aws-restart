import random
print("Welcome to guess the number! ")
print("The rules are simple, i will think of a number, and you will try to guess it ")
number = random.randint(1,10)
IsGuessRight = False
while IsGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! you win! ".format(guess))
        isGuessRight = True
    else: 
        print("you guessed it {} sorry that isn´t. try again.".format(guess))

