def variable_args(*args, **kwargs):    
#Prints positional and keyword arguments.
    print(f"Positional args: {args}")
    print(f"Keyword args: {kwargs}")

variable_args(1, 2, 3, name="Bob", role="Developer")