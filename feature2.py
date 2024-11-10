def sum_of_squares(numbers):
    # Corrected to sum the squares of each number
    return sum(n**2 for n in numbers)  # Now sums n**2 for each n in numbers

if __name__ == "__main__":  # Fixed variable names to __name__ and __main__
    test_numbers = [1, 2, 3, 4]

    # Additional feature: Print the squares of the numbers
    squares = [n**2 for n in test_numbers]
    print("Squares of the numbers:", squares)

    print("Sum of squares:", sum_of_squares(test_numbers))  # Expected output: 30
