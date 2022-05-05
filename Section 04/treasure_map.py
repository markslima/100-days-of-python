# 🚨 Don't change the code below 👇
from time import CLOCK_MONOTONIC
from tkinter.tix import COLUMN

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

map_row = int(position[0]) - 1
map_column = int(position[1]) - 1

# print(f"You picked row {map_row}")

map[map_row][map_column] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")