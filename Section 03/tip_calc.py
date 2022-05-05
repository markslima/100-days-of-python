#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? %"))
people = int(input("How many people to split the bill? "))
#print(f"Each person should pay: ${total}")


tip = percentage * .01
bill_tip = bill * tip
total = bill + bill_tip
each_tip = bill_tip / people
portion = round( total / people, 2)

print(f"\n\nOkay, then.. so with a bill of ${bill}, \nand you are generously choosing to go with %{percentage} for a tip, \nand there are {people} of you, let's see.. \nthat brings the total bill to ${total}. Your tip alone is ${each_tip} each and we again thank you for your kindness.\nEvenly divided, that makes for ${portion} from each of you.\n\nMerci, bon jour!")