from random import randint


lower_bound, upper_bound = 1, 20
adaptive_lower_bound = lower_bound
adaptive_upper_bound = upper_bound

to_be_guessed = randint(lower_bound, upper_bound)
print(to_be_guessed)
guess = 0
number_guesses = 0
max_guesses = 6
succeeded = False
giving_up = False

for _ in range(max_guesses + 1):
    if guess != to_be_guessed:
        try:
            print("used", number_guesses, "guess(es)",
                  "still have", max_guesses - number_guesses, "guesses left")
            guess = int(input("New number: "))
            number_guesses += 1
            if guess <= 0:  # <= 0 means giving up
                giving_up = True
                print("Sorry that you're giving up!")
                break  # break out of a loop, don't execute "else"
            elif guess < lower_bound or guess > upper_bound:
                print("Guess not within boundaries")
            elif guess < adaptive_lower_bound \
                    or guess > adaptive_upper_bound:
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
        succeeded = True
        print("Congratulations. You made it!")
        break

if succeeded is False and giving_up is False:
    print(f"So sorry, you have used {max_guesses} guesses but haven't succeeded.")
