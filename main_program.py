from math_operations import MathOperations

class MainProgram(MathOperations):
    def input_numbers(prompt):
        while True:
            try:
                number = float(input(prompt))
            except ValueError:
                (print("Please enter a valid number."))

    def calculator(self):
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
                        print(f"Result: {first_number} + {second_number} = {self.addition(first_number, second_number)}")
                    elif user_choice == "2":
                        print(f"Result: {first_number} - {second_number} = {self.subtraction(first_number, second_number)}")
                    elif user_choice == "3":
                        print(f"Result: {first_number} x {second_number} = {self.multiplication(first_number, second_number)}")
                    elif user_choice == "4":
                        print(f"Result: {first_number} / {second_number} = {self.division(first_number, second_number)}")
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error: {e}")
                repeat = input("Would you like to repeat the operation? (y/n): ").strip().lower()
                if repeat != "y" and repeat != "yes":
                    print("Thank you!")
                    break

if __name__ == '__main__':
    main_program = MainProgram()
    main_program.calculator()

