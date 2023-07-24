# Functions with Outputs

def format_name(f_name, l_name):
    """
    Take a first and last name and format it to return
    the title case version of the name
    """
    if l_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    return f_name.title() + " " + l_name.title()


print(format_name("anGEla", "BaUER"))
print(format_name("", ""))
