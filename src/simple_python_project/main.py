# Project_cicd/src/main.py


def add_numbers(a, c):
    return a + c

# subraction function
def subtract_numbers(a, b):
    return a - b


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    print(f"Addition: {add_numbers(num1, num2)}")
    print(f"Subtraction: {subtract_numbers(num1, num2)}")


if __name__ == "__main__":
    main()


# To run the tests, execute the following command:
# export PYTHONPATH=./src
# pytest
