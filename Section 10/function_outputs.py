

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Nothing here"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}, fuck yeah."

print(format_name(input("What is your firstname: "), input("What is your last name: ")))