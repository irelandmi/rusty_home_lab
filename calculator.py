import operator

def calculate(num1, num2, operation):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '//': operator.floordiv,
        '%': operator.mod
    }
    return ops[operation](num1, num2)

def main():
    print("Python Calculator CLI")
    print("Supported operations: +, -, *, /, **, //, %")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation: ")
            
            result = calculate(num1, num2, operation)
            print(f"Result: {result}")
            
            if input("Continue? (y/n): ").lower() != 'y':
                break
        except (ValueError, ZeroDivisionError, KeyError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
