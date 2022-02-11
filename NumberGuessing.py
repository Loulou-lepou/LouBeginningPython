# Number guessing game
# A human player has to guess a number between a range.
# The player inputs his guess.
# The program informs the player, if the number is larger, smaller or equal to a secret number, i.e,
# the number which the program has randomly created.
# If the player wants to give up, he or she can input a 0 or a negative number.

from random import randint


upper_bound = 20
lower_bound = 1
adaptive_lower_bound = lower_bound
adaptive_upper_bound = upper_bound

to_be_guessed = randint(lower_bound, upper_bound)
guess = 0
while guess != to_be_guessed:
    try:
        guess = int(input("New number: "))
        if guess <= 0:  # <= 0 means giving up
            print("Sorry that you're giving up!")
            break  # break out of a loop, don't execute "else"
        elif guess < lower_bound or guess > upper_bound:
            print("Guess not within boundaries")
        elif guess < adaptive_lower_bound or guess > adaptive_upper_bound:
            print("Your guess is contradictory to your previous guesses!")
        else:
            if guess > to_be_guessed:
                adaptive_upper_bound = guess - 1
                print("Number too large")
            elif guess < to_be_guessed:
                adaptive_lower_bound = guess + 1
                print("Number too small")
    except ValueError:
        print("you have to enter an integer")
        pass
else:
    print("Congratulations. You made it!")
