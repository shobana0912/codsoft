def calculator():
    print("\t \t \t SIMPLE CALCULATOR\t \t \t")
    print("Operations: +  -  *  /  **  //  (Type 'exit' to quit)")
    while True:
        num1 = input("Enter the first number: ")
        if num1.lower() == 'exit':
            break
        num2 = input("Enter the second number: ")
        if num2.lower() == 'exit':
            break
        op = input("Enter an operation (+  -  *  /  **  //): ")
        if op.lower() == 'exit':
            break
        try:
            num1, num2 = float(num1), float(num2)
            if op == '+': result = num1 + num2
            elif op == '-': result = num1 - num2
            elif op == '*': result = num1 * num2
            elif op == '/': result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            elif op == '': result = num1 ** num2
            elif op == '//': result = num1 // num2 if num2 != 0 else "Error: Division by zero"
            else: result = "Invalid operation"
        except ValueError:
            result = "Invalid input. Please enter numbers."
        print(f"Result: {result}\n")
calculator()
