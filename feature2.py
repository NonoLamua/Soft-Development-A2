def sum_of_squares(numbers):
    # Bug: Incorrectly sums numbers instead of their squares
    return sum(numbers)

if _name_ == "_main_":
    test_numbers = [1, 2, 3, 4]
    print("Sum of squares:", sum_of_squares(test_numbers))  # Expected output: 30, but returns 10