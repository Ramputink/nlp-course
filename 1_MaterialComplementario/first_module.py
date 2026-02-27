
def join_name(first_name,surname):
# Take the first name in the first parameter and the surname, both as strings, and return the name joined. Example: join_name("Jose","Alonso") should returns "Jose Alonso"
  return first_name + ' ' + surname

def split_name(full_name):
# Take a full name, split it and add each element to a list. Example: split_name("Jose Alonso") should returns ["Jose","Alonso"]
  return full_name.split()

def invert_name(full_name):
# Take a full name, split them, and returns an string with the surname first, a comma, and the first name. Example: invert_name("Jose Alonso") should returns "Alonso, Jose"
  list_names=split_name(full_name)
  return ', '.join(list_names[::-1])
