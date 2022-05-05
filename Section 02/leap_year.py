year = int(input("which year do you want to check? "))
candidate = year

# on every year that is evenly divisible by 4
# EXCEPT every year that is evenly divisible by 100;
# UNLESS the year is also evenly divisible by 400;

if year % 4 != 0:
    print(f"Not a leap year. Bummer!")
elif candidate % 100 != 0:
    print(f"Happy Leap Year! Go vote!")
elif candidate % 400 == 0:
    print(f"Alright! Happy Leap Year!")
else:
    print(f"Not a leap year. Bummer.")
    








#     print(f"Happy Leap Year! Go vote!")
# else:
#     print(f"Oh, awkward. No Leap Year this year!")
