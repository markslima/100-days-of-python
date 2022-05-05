import random

# example names list
# rose,sylvia,christine,charlie,mary,poppy,peter

names = input("\nSo who did you have lunch with today? \nPlease separate names with commas! \n\n")

name_list = names.split(",")
# print(name_list)

# namess = ['jimmy', 'bob', 'saul', 'bertrand']

# how_many = len(name_list)
# chosen = random.randint(0, how_many - 1)
payee = random.choice(name_list)
print(f"\n\nSo it looks like {payee} is buying lunch today! Thanks {payee}!\n")
# print(f"there are {how_many} elements in this list!")
