from random import randint

# dictionary containing customized settings of each levels
levels = {
    "1": {
        "name": "Easy",
        "start_message": ""f"What's the secret number to the treasure Chest",
        "min_num": 1,
        "max_num": 6,
        "guesses": 6
    },
    "2": {
        "name": "Medium",
        "start_message": "Guess the secret number to open the safe",
        "min_num": 1,
        "max_num": 20,
        "guesses": 4
    },
    "3": {
        "name": "Hard",
        "start_message": "Guess the secret number to the unlock the vault",
        "min_num": 1,
        "max_num": 50,
        "guesses": 3
    }
}


# function for game play dialog
def play_game():
    while True:
        play = input("Yes/No: ")
        if play.lower() == "yes":
            start()
        elif play.lower() == "no":
            print("Okay, maybe next time!")
            exit(0)
        else:
            print("Wrong input!")


# function to be used for each levels when selected
def game(level):
    game_plot = levels[level]  # assigning each key in the "levels" dictionary to the variable
    number = randint(game_plot["min_num"], game_plot["max_num"])  # setting the level secret number
    print(number)
    print(f"{game_plot['start_message']}\nYou have {game_plot['guesses']} number of guess(es) left.")

    while True:
        try:
            answer = input(f"hint: number is between {game_plot['min_num']} and {game_plot['max_num']}?\nAnswer: ")
            game_plot["guesses"] -= 1

            if int(answer) == number:
                # if user gets the answer while in level 3
                if level == "3":
                    print("You win the game!\nRestart Game?")
                    play_game()
                # if user gets the answer in other levels
                print("You got it right!\nEnter next level?")
                while True:
                    next_level = input("Yes/No: ")
                    if next_level.lower() == "yes":
                        game(str(int(level) + 1))
                    elif next_level.lower() == "no":
                        print("Okay, maybe next time!")
                        exit(0)
                    else:
                        print("Wrong input!")
            # if user doesn't get the answer and has no more guesses left
            elif game_plot["guesses"] == 0:
                print("You have no more guesses left.\nYou lose!")
                print("Do you want to play again")
                play_game()
            # if user does not get the answer and still has guesses
            else:
                print(f"Wrong try again!\nYou have {game_plot['guesses']} guess(es) left")
        # if user enters anything other than a number
        except ValueError:
            print(f"Please enter a number!\nYou have {game_plot['guesses']} guess(es) left")


# function that starts the game
def start():
    print("Select your difficulty level\nEasy: 1\nMedium: 2\nHard: 3")
    while True:
        try:
            level = input("Enter level number: ")
            if level == "1" or level == "2" or level == "3":
                game(level)  # python uses the level selected to call the game function
            else:
                print("Wrong input!")
        except ValueError:
            print(f"Please enter a number!")


# Game intro
print("Hi gamer, Welcome to Number Guess!\nAre you ready to play?")
play_game()
