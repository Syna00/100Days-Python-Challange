def format_name(f_name, l_name):
    """Take a first and last name and format it to return the 
    title case version of the name"""
    formated_f_name = f_name.title()
    foramted_l_name = l_name.title()
    return(f"{formated_f_name} {foramted_l_name}")

output = format_name("seto", "wahyudi")
print(output)