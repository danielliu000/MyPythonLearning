my_string = 'we are fine.'

def replace_space(my_str):

    my_str = str(my_str)

    new = '%20'.join(my_str.split(' '))
    print(new)


replace_space(my_string)
