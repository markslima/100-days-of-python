from game_data import data
from random import randint
from art import logo, vs

def cls():
    print("\n" * 80)

playing = True

score = 0


 
while playing == True:


    random1 = randint(0, len(data) - 1)
    guess_a = data[random1]

    random2 = randint(0, len(data) - 1)
    guess_b = data[random2]

    

    print(f"\n\n{logo}")
    compare_a = (guess_a['follower_count'])
    # REMOVE added follower_count for game testing
    print(f"Compare A: {guess_a['name']}, a {guess_a['description']}, from {guess_a['country']}.")

    print(vs)
    compare_b = (guess_b['follower_count'])
    # REMOVE added follower_count for game testing
    print(f"Compare B: {guess_b['name']}, a {guess_b['description']}, from {guess_b['country']}.")

    # print(f"Here is the last guess A: {keep_guess_a}")
    guess = input("\nWho has more followers? Type 'A' or 'B': ").lower()

    if guess == 'a':
        if (compare_a) - (compare_b) > 0:
            score += 1
            print(f"\nYou're right! 🎉 Current score: {score}")
            # guess_a = keep_guess_a
            
        else:
            cls()
            print(f"Sorry, that's wrong. 😭 Final score: {score}\n")
            playing = False
            
    elif guess == 'b':
            if (compare_b) - (compare_a) > 0:
                score += 1
                print(f"\nYou're right! 🎉 Current score: {score}")
                # guess_b = keep_guess_a
            else:
                cls()
                print(f"Sorry, that's wrong. 😭 Final score: {score}\n")
                playing = False


