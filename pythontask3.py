from random import randint


def level_three():
    guess_count = 3
    number = randint(1, 50)
    print(number)
    print(f"Guess the secret number to the unlock the vault\nYou have {guess_count} guesses")
    while True:
        try:
            answer = input("hint: number is between 1 and 50?\nAnswer: ")
            guess_count -= 1
            if int(answer) == number:
                print("You win the game!\nRestart Game?")
                while True:
                    restart_game = input("Yes/No: ")
                    if restart_game.lower() == "yes":
                        start()
                    elif restart_game.lower() == "no":
                        print("Okay, maybe next time!")
                        exit(0)
                    else:
                        print("Wrong input!")
            elif guess_count == 0:
                print("You have no more guesses left.\nYou lose!")
                print("Do you want to play again")
                while True:
                    play_again = input("Yes/No: ")
                    if play_again.lower() == "yes":
                        start()
                    elif play_again.lower() == "no":
                        print("Okay, maybe next time!")
                        exit(0)
                    else:
                        print("Wrong input!")
            else:
                print(f"Wrong try again! you have {guess_count} guess(es) left")
        except ValueError:
            print(f"Please enter a number!\nYou have {guess_count} guess(es) left")


def level_two():
    guess_count = 4
    number = randint(1, 20)
    print(number)
    print(f"Guess the secret number to open the safe\nYou have {guess_count} guesses")
    while True:
        try:
            answer = input("hint: number is between 1 and 20?\nAnswer: ")
            guess_count -= 1
            if int(answer) == number:
                print("You got it right!\nEnter next level?")
                while True:
                    next_level = input("Yes/No: ")
                    if next_level.lower() == "yes":
                        level_three()
                    elif next_level.lower() == "no":
                        print("Okay, maybe next time!")
                        exit(0)
                    else:
                        print("Wrong input!")
            elif guess_count == 0:
                print("You have no more guesses left.\nYou lose!")
                print("Do you want to play again")
                while True:
                    play_again = input("Yes/No: ")
                    if play_again.lower() == "yes":
                        start()
                    elif play_again.lower() == "no":
                        print("Okay, maybe next time!")
                        exit(0)
                    else:
                        print("Wrong input!")
            else:
                print(f"Wrong try again! you have {guess_count} guess(es) left")
        except ValueError:
            print(f"Please enter a number!\nYou have {guess_count} guess(es) left")


def level_one():
    guess_count = 6
    number = randint(1, 10)
    print(number)
    print(f"What's the secret number to the treasure Chest\nYou have {guess_count} guesses")
    while True:
        try:
            answer = input("hint: number is between 1 and 10?\nAnswer: ")
            guess_count -= 1
            if int(answer) == number:
                print("You got it right!\nEnter next level?")
                while True:
                    next_level = input("Yes/No: ")
                    if next_level.lower() == "yes":
                        level_two()
                    elif next_level.lower() == "no":
                        print("Okay, maybe next time!")
                        exit(0)
            elif guess_count == 0:
                print("You have no more guesses left.\nYou lose!")
                print("Do you want to play again")
                while True:
                    play_again = input("Yes/No: ")
                    if play_again.lower() == "yes":
                        pass
                    elif play_again.lower() == "no":
                        print("Okay, maybe next time!")
                        exit(0)
                    else:
                        print("Wrong input!")
            else:
                print(f"Wrong try again! you have {guess_count} guess(es) left")
        except ValueError:
            print(f"Please enter a number!\nYou have {guess_count} guess(es) left")


def start():
    print("Select your difficulty level\nEasy: 1\nMedium: 2\nHard: 3")
    while True:
        level = input("Enter level number: ")
        if level == "1":
            level_one()
        elif level == "2":
            level_two()
        elif level == "3":
            level_three()
        else:
            print("Wrong input!")


print("Hi gamer, Welcome to Number Guess!\nAre you ready to play?")
while True:
    ready = input("Yes/No: ")
    if ready.lower() == "yes":
        start()
    elif ready.lower() == "no":
        print("Okay, maybe next time!")
        exit(0)
    else:
        print("Wrong input!")
