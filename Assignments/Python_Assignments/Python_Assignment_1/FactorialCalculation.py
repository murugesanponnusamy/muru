def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Prompt user for input
while True:
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Calculate and display the factorial number
result = calculate_factorial(num)
print(f"Factorial of {num} is {result}.")