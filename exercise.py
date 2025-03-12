# Return the First name

name = 'Titilope Olatunji'

def first_name(f_name):
    """
    This function takes the full name as input and returns the first name

    Args:
        The full name of the person
    
    Returns:
        The first name
    """
    first_name = name.split()
    return first_name[0]

name  = 'Titilope Olatunji'

print(first_name(name))

# Return the Last name

def last_name(l_name):
    """
    This function takes the full name as input and returns the last name

    Args:
        The full name of the person
    
    Returns:
        The last name
    """
    last_name = name.split()
    return last_name[1]

name  = 'Titilope Olatunji'

print(last_name(name))

# Return the Full name

def full_name(fl_name):
    """
    This function takes the full name as input and returns the first name and the last name from the above functions

    Args:
        The full name of the person
    
    Returns:
        The full name
    """
    get_first_name = first_name(name)
    get_last_name = last_name(name)
    full_name = f'My full name is {get_first_name} {get_last_name}'
    return full_name

name  = 'Titilope Olatunji'

print(full_name(name))


# Return list with the same naming convention

names= ['first name', 'last_name', 'date of birth']

def name_dob(name_x):
    """
    This is a list of string with different naming convention, 
    transform the list to have the same naming convention
    Args:
        A list of string 
    Returns: 
        The list with the same naming convention
    """
    result=[]
    for name in names:
        if not name == '_':
            name =name.replace(" ", "_")
            result.append(name)
    return result

names= ['first name', 'last_name', 'date of birth']
print(name_dob(names))


# Return the list of names that start with capital letter and ends with 'a'

list_of_names =['Mayowa', 'chizoba', 'Chigozie']

def extract_names(names):
    """
    This function checks for names that starts with a capital letter and ends with letter 'a' and change 
    the name that start with a capital letter but doesn't end with 'a' to 'a'

    Args:
        A list of strings(names)
    
    Returns:
        Names that begins with capital letter and ends with a
    """
    result_with_capital_letter =[]
    result_end_with_a=[]
    for name in list_of_names:
        if name[0].isupper() and name[1].islower():
            result_with_capital_letter.append(name)
            if not name.endswith('a'):
                name =name[:-1] +'a'
                result_end_with_a.append(name)


    for get_names in result_with_capital_letter:
        if get_names.startswith('M'):
             result_end_with_a.append(get_names)
    return result_end_with_a
        
list_of_names =['Mayowa', 'chizoba', 'Chigozie']
        
print(extract_names(list_of_names))


# Raises an error for an invalid name

names=['Wofai', 'Zainab', 'A4atullah']


def customers_name(valid_names):
    """
    This function checks if the list of names are valid. Valid names contains only alphabetic character

    Args:
        A list of names to be validated
    
    Returns: 
        Raises a ValueError with invalid name
    """
    result=[]
    for name in names:
        if not name.isalpha():
            result.append(name)
            raise ValueError(f"The name {name} is not a valid name")
    return result


try:
    names =['Wofai', 'Zainab', 'A4atullah']
    print(customers_name(names))  
except ValueError as a:
    print(a)




