print("Weclome to the rollercoaster!")
height = int(input("What is your height? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("And what is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18 and age < 21:
        print("Please pay $7")
    elif age >= 21:
        print("That will be $500 yes you heard that right. Get the fuck outta here.")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to be taller than 120cm before you can ride, shorty.")