formatted_name = print(format_name(input("What is your firstname: "), input("What is your last name: ")))

length = len(formatted_name)

def format_name(f_name, l_name):
    """
    Take a first and last name and format it
    to return the title case version of the name.
    """
    if f_name == "" or l_name == "":
        return "Nothing here"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}, fuck yeah."

format_name()