def describe_person(name, age, *, city, profession):
#Prints a formatted introduction of a person.
    print(f"{name} is {age} years old and works as a {profession} in {city}.")

def variable_args(*args, **kwargs):    
#Prints positional and keyword arguments.
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

# Example usage
describe_person("Alice", 30, city="New York", profession="Engineer")
variable_args(1, 2, 3, name="bob", role="Developer")