#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from guess_art import logo
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_answer(guess, number, turns):
    if guess > number:
        print("Too high.\nGuess again.")
        return turns - 1
    elif guess < number:
        print("Too low.\nGuess again.")
        return turns -1
    elif guess == number:
        print(f"\n*** You guessed my number: {number}! Well done! ***\n")

def difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if level == "easy":
        return EASY_ATTEMPTS
    elif level == "hard":
        return HARD_ATTEMPTS

def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    print(f" Today's random number is {answer}")

    turns = difficulty()
    print(f"You have {turns} left to play.")

    guess = 0
    while guess != answer:
        guess = int(input("Make a guess: "))
        check_answer(guess, answer, turns)
        if turns == 0:
            print("Game over!")
            break

game()