def format_name(f_name, last_name):
  """Takes a first and last name and formats it to give
  a title case of the name"""
  if not f_name or not last_name:
    return "I'm gonna need both names to run!!"


  name_caps = f_name + ' ' + last_name
  return name_caps.title()

my_name = format_name(input("what is your first name?"), input("what is your last name?"))

print(my_name)