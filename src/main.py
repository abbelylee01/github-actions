# simple_python_project/main.py

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

if __name__ == "__main__":
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Addition: {add_numbers(num1, num2)}")
    print(f"Subtraction: {subtract_numbers(num1, num2)}")
