# Basic example of a python decorator function

def decorator_function(original_function):
    def wrapper_function(*args):
        print(f'I am going to call {original_function.__name__}')
        original_function(*args)
        print(f'{original_function.__name__} has finished')

    return wrapper_function


@decorator_function
def display_person_info(name, age, job_title, location):
    print(f'{name} is {age} years old and works as {job_title} in {location}')


decorator_function(display_person_info)('John', 25, 'Data scientist', 'Bangalore')
