# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

score = 0
lower_name1 = name1.lower()
lower_name2 = name2.lower()
names = lower_name1 + lower_name2

t = names.count('t')
r = names.count('r')
u = names.count('u')
e = names.count('e')
true_total = (t + r + u + e)

l = names.count('l')
o = names.count('o')
v = names.count('v')
e = names.count('e')
love_total = (l + o + v+ e)

score = str(true_total) + str(love_total)

if int(score) < 10 or int(score) > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) > 40 and int(score) < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
