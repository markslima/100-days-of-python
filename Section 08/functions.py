alphabet = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


def greet(something):
    print(something)
    print('\n')
    print("how are you doing?")
    print("lovely weather we're having, isn't it?")
    print("i want a divorce, and i'm taking the kids and house.")
    print('\n')

greet('hey baby')

# functions with more than one parameter
def greet_with(name, location):
    print(f"Hello {name} from {location}")

greet_with('mark', 'chicago')
print('\n')
greet_with(location='toronto', name='orit')