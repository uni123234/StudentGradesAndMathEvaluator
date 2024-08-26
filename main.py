"""
This script includes a student grade check, an interactive math evaluator 
using basic arithmetic, and a quadrant checker based on input coordinates.
"""

import operator

# Define safe operations
OPERATIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


def safe_eval(expression):
    """Evaluates a basic arithmetic expression safely."""
    try:
        parts = expression.split()
        if len(parts) != 3:
            raise ValueError("Expression must be in the form 'a + b'")

        num1, op, num2 = parts
        num1 = float(num1)
        num2 = float(num2)

        if op in OPERATIONS:
            result = OPERATIONS[op](num1, num2)
        else:
            raise ValueError("Unsupported operation")
        return result
    except ValueError as e:
        return f"ValueError: {e}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except (TypeError, IndexError) as e:
        return f"Error: {e}"


# Checking student grades
NAME_L = input("Ваше прізвище: ")
BAL = int(input("Ваші бали за семестр: "))

if BAL >= 80:
    print(f"Студент {NAME_L} здав іспит")
else:
    print(f"Не здав іспит {NAME_L}")

# Interactive math evaluator (using safe_eval)
while True:
    OPR = input("Введіть приклад (наприклад, '3 + 4'): ")
    print(safe_eval(OPR))

# Quadrant checker
X = float(input("Введіть число x: "))
Y = float(input("Введіть число y: "))

if X > 0 and Y > 0:
    KL = 1
elif X < 0 and Y > 0:
    KL = 2
elif X < 0 and Y < 0:
    KL = 3
elif X > 0 and Y < 0:
    KL = 4
else:
    KL = 0

print(f"x = {X}, y = {Y}, {KL} четверть.")
