def print_even_numbers():
    try:
        numbers = input("Enter numbers: ")
        num_list = [int(num.strip()) for num in numbers.split(",")]
        even_numbers = [num for num in num_list if num % 2 == 0]
        
        print("Even numbers :", even_numbers)
    except ValueError:
        print("Invalid input! Please enter only numbers separated by commas.")

print_even_numbers()