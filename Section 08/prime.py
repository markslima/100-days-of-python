#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if (number % i == 0):
            is_prime = False
    if is_prime:
        print(f"The number {number} is a PRIME!")
    else:
        print(f"{number} is NOT prime.")

def cls():
    print("\n" * 10)



cls()
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)