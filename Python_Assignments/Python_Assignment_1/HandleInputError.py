def print_even_numbers():
    while True:
        try:
            numbers = input("Enter numbers: ")
            num_list = [int(num.strip()) for num in numbers.split(",")]
            even_numbers = [num for num in num_list if num % 2 == 0]
            
            print("Even numbers:", even_numbers)
            break
        except ValueError:
            print("Invalid input detected! Please enter only numbers.")

print_even_numbers()