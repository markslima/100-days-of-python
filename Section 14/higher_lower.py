from game_data import data
from random import randint
from art import logo, vs

def cls():
    print("\n" * 40)

playing = True

score = 0
# user input:  "Who has more followers? Type 'A' or 'B": 
while playing == True:
# def play_game():
    random1 = randint(0, len(data) - 1)
    random2 = randint(0, len(data) - 1)

    guess_a = data[random1]
    guess_b = data[random2]

    print(logo)
    compare_a = (guess_a['follower_count'])
    print(f"Compare A: {guess_a['name']}, a {guess_a['description']}, from {guess_a['country']}.")

    print(vs)
    compare_b = (guess_b['follower_count'])
    print(f"Compare B: {guess_b['name']}, a {guess_b['description']}, from {guess_b['country']}.")

    # print(f"This is inside the play_game() function {guess_a['name']}")
    # print(f"This is also inside the play_game() function {guess_b['name']}")
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    # select comparison depending on user input (if/else ?)
    if guess == 'a':
        if (compare_a) - (compare_b) > 0:
        # if (guess_a['follower_count'] - guess_b['follower_count']) > 0:
            score += 1
            print(f"\nYou're right! 🎉 Current score: {score}")
        else:
            cls()
            print(f"Sorry, that's wrong. 😭 Final score: {score}\n")
            playing = False
            
    elif guess == 'b':
            if (guess_b['follower_count'] - guess_a['follower_count']) > 0:
                score += 1
                print(f"\nYou're right! 🎉 Current score: {score}")
            else:
                cls()
                print(f"Sorry, that's wrong. 😭 Final score: {score}\n")
                playing = False
                
            
                    
                    







## Game NOTES ##
# random1 = randint(0, len(data) - 1)
# random2 = randint(0, len(data) - 1)

#
# guess_a = data[random1]
# guess_b = data[random2]
## print higher/lower ascii art
# print(logo)

# "Compare A: {randomly_selected_comparison1"
# compare_a =("{data[random1]['follower_count']}")
# print(f"Compare A: {guess_a['name']}, a {guess_a['description']}, from {guess_a['country']}.")
# print Vs. ascii art
# print(vs)

# "Against B: {randomly_selected_comparison2"
# print(f"Compare B: {guess_b['name']}, a {guess_b['description']}, from {guess_b['country']}.")

## /// ##

# while playing == True:  
#     play_game()
# compare data.follower_count between A and B
# print(f"You have selected {guess}, {guess_b['name']}, with {guess_b['follower_count']}")

# f"You're right! Current score: {score}
# f"Sorry, that's wrong. Finale score: {score}"
#
# keep looping game:
#
# while right == True:
#   play_game()
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 