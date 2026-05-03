from math_operations import MathOperations

class MainProgram(MathOperations):
    def input_numbers(prompt):
        while True:
            try:
                number = float(input(prompt))
            except ValueError:
                (print("Please enter a valid number."))

    def calculator():
        while True:
            print("Welcome to Python Simple Calculator")
            print("Please choose the operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            user_choice = str(input("Please choose the operation from 1-4: "))
            if user_choice in ("1", "2", "3", "4"):
                try:
                    first_number = float(input("Please enter the first number: "))
                    second_number = float(input("Please enter the second number: "))
                    if user_choice == "1":
                        print()
