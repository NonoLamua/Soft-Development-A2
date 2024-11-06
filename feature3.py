# feature3.py

import math

def square_roots(numbers):
    # Bug: Does not handle negative numbers, which will cause a math domain error
    return [math.sqrt(x) for x in numbers]

if _name_ == "_main_":
    test_numbers = [4, 9, -16, 25]
    print("Square roots:", square_roots(test_numbers))  # Expected error due to -16