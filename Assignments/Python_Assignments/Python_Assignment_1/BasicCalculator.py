def calculator():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            operation = input("Choose operation (+, -, *, /): ")
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation! Please enter one of +, -, *, or /.")
                continue
            
            print(f"Result : {num1} {operation} {num2} = {result}")
            break
        except ValueError:
            print("Invalid input! Please enter numeric values.")

calculator()