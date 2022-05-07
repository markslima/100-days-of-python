
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# word_list_length = len(word_list)
# secret_choice = random.randint(0, word_list_length - 1)

import random
# random.choice is the modern way to randomly pick from iterable
chosen_word = random.choice(word_list)

guess = input(f"\nGuess: ").lower()

# secret_word_letters = list(chosen_word)

print(f"\nThe secret word was {chosen_word}\n")

for letter in chosen_word:
    if letter == guess:
        print("CORRECT")
    else:
        print("WRONG")



# if choice in secret_word:
#     print("CORRECT")
# else:
#     print("WRONG")


print(f"Your choice was {letter}")

