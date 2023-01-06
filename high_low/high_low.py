import random


def check_user():
    print("Hey")


def play_game():
    print("--------------GAME STARTING--------------\n\n")

    current_nbr = random.randint(1, 10)
    print("Current number is: " + str(current_nbr))

    while True:
        user_guess = input("Do you think is Higher or Lower? (H/L)\n")
        if user_guess == "H" or user_guess == "L":
            break
        else:
            print("Oops Invalid Input! Try Again")

    next_random_nbr = random.randint(1, 10)

    if user_guess == "H" and next_random_nbr > current_nbr:
        print("YOU NAILED IT!")
    elif user_guess == "L" and next_random_nbr < current_nbr:
        print("YOU NAILED IT!")
    else:
        print("Hard Luck :/")

    print("Number was: "+str(next_random_nbr))
    print("--------------GAME ENDED! Thank you for playing :) --------------\n\n")


play_value = "Y"
while play_value == "Y":
    play_game()
    while True:
        play_value = input("Play Again? (Y/N)\n")
        if play_value == "Y" or play_value == "N":
            break
        else:
            print("Oops Invalid Input! Try Again")

print("Thanks for playing! Hope You Enjoyed It :)")