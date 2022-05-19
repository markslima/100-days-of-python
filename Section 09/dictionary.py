programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    }

programming_dictionary["Variable"] = "A placeholder for data"

# print(programming_dictionary)

empty_dictionary = {}

for key in programming_dictionary:
    print(f'Key: {key}')
    print(f'Value: {programming_dictionary[key]}\n')
