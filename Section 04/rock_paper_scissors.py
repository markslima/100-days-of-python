import random

computer_choice = random.randint(0,2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input(f"\n\nWhat do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if choice >= 3 or choice <= 0:
  print(f"\nYou aren't choosing the correct number. It must be between 1 and 3.\n")

print(f"\nThe computer has chosen: {computer_choice}\n")

if choice == 0 and computer_choice == 1:
  print(f"You lose! PAPER beats ROCK!")
  print(paper)
elif choice == 0 and computer_choice == 2:
  print(f"You win! ROCK beats SCISSORS!")
  print(rock)

if choice == 1 and computer_choice == 2:
  print(f"You lose! SCISSORS beats PAPER!")
  print(scissors)
elif choice == 1 and computer_choice == 0:
  print(f"You win! PAPER beats ROCK!")
  print(paper)

if choice == 2 and computer_choice == 0:
  print(f"You lose! Rock beats SCISSORS!")
  print(rock)
elif choice == 2 and computer_choice == 1:
  print(f"You win! SCISSORS beats PAPER!")
  print(scissors)
elif choice == computer_choice:
  print(f"It's a DRAW! No one wins!\n")

