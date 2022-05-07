import random

# list(word)

words = ['chair', 'foot', 'car', 'reminder', 'calendar', 'violin', 'star', 'rocket', 'tapioca', 'book', 'pen','phone', 'stove']

def random_word(word_list):
    number_of_words = len(word_list)
    selection = random.randint(0, number_of_words - 1)
    return word_list[selection]

secret= random_word(words)

choice = input(f"\nAll right, then give me a letter: ")

secret_length = len(secret)

score = secret_length

if secret_length == 0:
    print(f"You have been hung, you are hanging dead for all to see. 😟  \n")
    score -= score 
elif choice in secret:
    print(f"\nYes, there is a {choice} in our word...")
else:
    print(f"Nope, you chose wrong! There is not a {choice}.\n")



print(f"The secret word length is: {secret_length}")
print(f"The secret word is: {secret}\n")
print(score)

