# Welcoming message for the user
print("Welcome to my calculator! Please follow the instructions to perform calculations.")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


def get_operator(prompt):
    valid_ops = ["+", "-", "*", "/", "**"]
    while True:
        op = input(prompt).strip()
        if op in valid_ops:
            return op
        print("Invalid operation. Please enter a valid operation (+, -, *, /, **).")


def apply_operation(x, op, y):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return x / y
    if op == "**":
        return x ** y
    raise ValueError("Unsupported operator.")


def calculator():
    while True:  # outer loop for repeated full calculations
        a = get_number("Enter the first number: ")
        while True:  # chaining loop: allow adding more numbers/operators to current result
            op = get_operator(
                "Enter the operation you want to perform (+, -, *, /, **): ")
            b = get_number("Enter the next number: ")
            try:
                a = apply_operation(a, op, b)
                print("Current result:", a)
            except ZeroDivisionError as zde:
                print("Error:", zde)
            # ask if user wants to continue chaining with the current result
            again = input(
                "Do you want to apply another operation to the current result? (yes/no): ").strip().lower()
            if again != "yes":
                break
        # ask if user wants to start a new calculation or exit
        restart = input(
            "Do you want to perform another calculation from scratch? (yes/no): ").strip().lower()
        if restart != "yes":
            print("Thank you for using my calculator! Goodbye!")
            break


if __name__ == "__main__":
    calculator()
