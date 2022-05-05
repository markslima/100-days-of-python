from typing import AsyncGenerator


age = input("What is your current age?")
age_as_int = int(age)
years_left  = (90 - age_as_int)

months = years_left * 12
weeks = years_left * 52
days = years_left * 365

message = f"You have {years_left} years, {months} months, and {days} days left.  Better get to it!!"

print(message)
