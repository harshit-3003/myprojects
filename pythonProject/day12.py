import random

EASY_LEVEL_TURNS = 10
Hard_Level_Turns = 5
turns = 0


def check_answer(user_guess, actual_answer, turns):
    if (user_guess < actual_answer):
        print("TOO LOW")
        print("guess again")
        return turns - 1
    elif (user_guess > actual_answer):

        print("TOO HIGH!")
        print("guess again")
        return turns - 1
    else:
        print(f"YES ! YOU GOT IT {actual_answer}")


def set_diffuculity():
    level = input("choose a difficulty level  Type 'easy' or 'hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS

    else:
        return Hard_Level_Turns


def game():
    print("Welcome to the guessing game!")
    print("i am thinking of a number")
    answer = random.randint(1, 100)

    turn = set_diffuculity()

    guess = 0
    while (guess != answer):
        print(f"you have{turn} attemps remaining to guess")
        guess = int(input("make a Guess:"))
        turn = check_answer(guess, answer, turn)
        if turn == 0:
            print("you ran out of guesses")
            exit()


game()

'''import random
Easy_Level_turns=10

Hard_level_turns=5
turns=0

def checkanswer(guess,answer,turns):
    if(guess < answer):
        print("TOO low")
        print("Guess low")

        return turns-1
    else:
        print("too high")
        print("Guess again")
        return turns-1
def set_level():
    level=input("choose a level u want to play (easy or hard)")
    if (level=="easy"):
        return Easy_Level_turns
    else:
        return Hard_level_turns



def game():
    print("welcome to the game")
    print("i am thinking oF A number")
    answer=random.randint(1,100)
    turns=set_level()
    guess=0
    while (guess != answer):
        print(f"you have {turns} left")
        guess=int(input("make  your Guess"))
        turns=checkanswer(guess,answer,turns)
        if turns==0:
            print("you hav no attemps left")
            exit()
game()'''
