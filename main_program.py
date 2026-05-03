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
            print()
